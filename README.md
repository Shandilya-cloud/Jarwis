🤖 Jarwis – Streamlit AI Chat Assistant

Jarwis is a Streamlit-based AI chat application powered by a locally hosted large language model (LLM) using an OpenAI-compatible API (such as LM Studio). The assistant is configured with a predefined system persona and maintains conversational memory during a session.

🚀 Features

💬 Interactive chat interface using Streamlit

🧠 Local LLM integration via OpenAI-compatible API

🔒 Hidden system prompt for persona control

🗂 Session-based conversation memory

⚙️ Configurable model and API endpoint

🛠 Simple and clean architecture

🏗 Architecture Overview

The application consists of:

Frontend: Built with Streamlit’s chat components

Backend LLM: Local model served via OpenAI-compatible API (e.g., LM Studio)

Session State: Stores conversation history

System Prompt: Controls assistant behavior

📦 Requirements

Python 3.8+

Streamlit

openai (Python SDK compatible with OpenAI API)

A locally running OpenAI-compatible server (e.g., LM Studio)

Install dependencies:
  pip install streamlit openai
  
⚙️ Configuration

Inside the script:

  LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
  LM_STUDIO_API_KEY = "lm-studio"
  MODEL_NAME = "local-model"
Required Setup

Start your local LLM server (e.g., LM Studio).

Ensure:

Server is running on http://localhost:1234

The loaded model supports /v1/chat/completions

Update MODEL_NAME if needed.

▶️ Running the Application
  streamlit run chatbots.py

The app will open in your browser.

🧠 How It Works

The system prompt defines the assistant's behavior.

User messages are stored in st.session_state.messages.

On each user input:

The system prompt + chat history is sent to the model.

The model generates a response.

The response is displayed and appended to session memory.

Message structure sent to the API:

[
    SYSTEM_PROMPT,
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."},
]
🗂 Project Structure
.
├── app.py
└── README.md
🔐 Persona Control

The assistant behavior is defined using a hidden system prompt:

SYSTEM_PROMPT = {
    "role": "system",
    "content": "Your name is Jarwis..."
}

You can modify this prompt to change tone, personality, or task specialization.

🎛 Customization Options

You can modify:

temperature for creativity

model name

Enable stream=True for streaming responses

Add persistent memory using a database

Add authentication for multi-user setups

🐛 Error Handling

Basic exception handling is included:

except Exception as e:
    assistant_reply = f"Error: {str(e)}"

You may extend this with:

Logging

Retry mechanisms

User-friendly error messages

🧩 Future Improvements

Streaming responses

Persistent chat history (database)

Multi-model support

Docker containerization

Deployment configuration

Environment variable configuration for secrets

UI enhancements

🛡 Security Notes

Do not hardcode API keys in production.

Use environment variables for sensitive configuration:

export LM_STUDIO_API_KEY="your-key"

Consider authentication if deploying publicly.

📄 License

This project is open-source and available for modification and distribution.

🙌 Acknowledgments

Built with Streamlit

Uses OpenAI-compatible API format

Compatible with local LLM servers such as LM Studio
