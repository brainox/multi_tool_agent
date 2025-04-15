# Multi-Tool Agent

This project is a multi-tool agent built using Google's Agent Development Kit (ADK). It demonstrates how to create an agent capable of handling multiple tools and interacting with users through a variety of interfaces.

## Features
- **Multi-tool integration**: Includes tools for weather and time queries.
- **Agent Development Kit (ADK)**: Utilizes Google's ADK for agent creation and management.
- **Extensible**: Easily add more tools and capabilities.

## Project Structure
```
multi_tool_agent/
├── __init__.py       # Initializes the module
├── agent.py          # Defines the agent and its tools
├── .env              # Environment variables (e.g., API keys)
└── __pycache__/      # Compiled Python files
```

## Prerequisites
- Python 3.9+
- [Google ADK](https://google.github.io/adk-docs/get-started/quickstart/)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/brainox/multi_tool_agent.git
   cd multi_tool_agent
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate    # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install google-adk
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root and add the following:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
   ```
   Replace `PASTE_YOUR_ACTUAL_API_KEY_HERE` with your actual Google API key.

## Running the Agent

1. **Start the Development UI**
   ```bash
   adk web
   ```

2. **Access the UI**
   Open the provided URL (e.g., `http://localhost:8000`) in your browser.

3. **Interact with the Agent**
   Use the UI to send queries like:
   - "What is the weather in New York?"
   - "What is the time in Paris?"

## Testing

To test the agent, you can run the following command:
```bash
adk run
```
This will execute the agent in the terminal, allowing you to interact with it directly.

## Documentation
For more details, refer to the [ADK Quickstart Guide](https://google.github.io/adk-docs/get-started/quickstart/).

## License
This project is licensed under the MIT License.