import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import requests

class EntertainmentAgent:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

        # Initialize the LLM instance
        self.llm = OpenAI(api_key=api_key)

    def get_recommendations(self, user_data):
        watched_titles = user_data.get('watched_titles', [])
        preferences = user_data.get('preferences', {})

        # Step 1: Create a prompt template and format it with user data
        prompt_template = PromptTemplate.from_template(
            "User preferences: {preferences}, watched titles: {watched_titles}. Suggest new movies to watch."
        )

        prompt = prompt_template.format(preferences=preferences, watched_titles=watched_titles)

        # Directly generate the response using the LLM
        enriched_request = self.llm(prompt)

        # Step 2: Send enriched request to service agents (Netflix, Apple, Hulu)
        service_urls = [
            'http://127.0.0.1:5002/netflix/recommend',
            'http://127.0.0.1:5003/apple/recommend',
            'http://127.0.0.1:5004/hulu/recommend'
        ]
        recommendations = []
        for url in service_urls:
            try:
                response = requests.post(url, json={'enriched_request': enriched_request, 'watched_titles': watched_titles})
                if response.status_code == 200:
                    recommendations += response.json()
            except requests.RequestException as e:
                print(f"Error communicating with {url}: {e}")

        return recommendations
