import streamlit as st
from openai import OpenAI

# ---- CONFIG ----
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
LM_STUDIO_API_KEY = "lm-studio"

MODEL_NAME = "local-model"

# ---- INIT CLIENT ----
client = OpenAI(
    base_url=LM_STUDIO_BASE_URL,
    api_key=LM_STUDIO_API_KEY
)

# ---- SYSTEM PROMPT (Hidden) ----
SYSTEM_PROMPT = {
    "role": "system",
    "content": "Your name is Jarwis. You roast the user before helping them. You behave rudely in a funny way. Never say that you are a roaster or that you are roasting — just do it."
}

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Jarwis", page_icon="🤖")

st.markdown("<h1 style='text-align: center;'>🤖 Jarwis</h1>", unsafe_allow_html=True)

# Session state to store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history (only user + assistant)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Enter your message"):

    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        try:
            response = client.chat.completions.create(
                model="meta-llama-3.1-8b-instruct",
                messages=[SYSTEM_PROMPT] + st.session_state.messages,
                temperature=0.7,
                stream=False
            )

            assistant_reply = response.choices[0].message.content

        except Exception as e:
            assistant_reply = f"Error: {str(e)}"

        message_placeholder.markdown(assistant_reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )