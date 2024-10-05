# Agent Marketplace

**Agent Marketplace** is a proof-of-concept application that facilitates interactions between user agents and service agents, leveraging AI for personalized recommendations. The system features an agent-driven architecture where agents autonomously communicate to provide movie suggestions based on user preferences and watch history.

## Features

- **User Agents**: User-specific agents (e.g., EntertainmentAgent) manage user preferences and history.
- **Service Agents**: Agents for services like Netflix, Apple, and Hulu provide recommendations.
- **Centralized Interaction**: EntertainmentAgent communicates with multiple service agents to gather and filter movie recommendations.
- **Local Movie Management**: SQLite database with a web interface to view and add movies to the user agent's history.

## Getting Started

### Prerequisites

- **Python 3.9+**
- **Flask** for creating web endpoints.
- **SQLite** for storing movies.
- **LangChain & OpenAI** for leveraging LLMs.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/agent-marketplace.git
   cd agent-marketplace
   ```
2. Set up a virtual environment and install dependencies:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file with your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your-openai-api-key
     ```

### Running the Application

1. **Initialize the SQLite Database**:
   ```sh
   python init_db.py
   ```
2. **Start the Flask Application**:
   ```sh
   python app.py
   ```
3. Access the web interface to manage movies:
   - Open your browser and go to `http://127.0.0.1:5001/movies`.

### Making Recommendations

- Use a tool like `curl` or Postman to make a recommendation request:
  ```sh
  curl -X POST http://127.0.0.1:5001/entertainment/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "watched_titles": ["The Dark Knight"],
    "preferences": {"genres": ["Sci-Fi", "Adventure"]}
  }'
  ```

## Project Structure

- **app.py**: Main Flask application with routes for managing movies and recommendations.
- **agents/**: Contains the agent classes (e.g., EntertainmentAgent, NetflixAgent).
- **templates/**: HTML files for the web interface.
- **movies.db**: SQLite database to store movie information.

## License

This project is open-source and available under the [MIT License](LICENSE).
