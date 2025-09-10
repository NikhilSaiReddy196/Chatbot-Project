import streamlit as st
import time
from test_inferance import bot

with st.sidebar:
    huggingface_api_key = st.text_input("Enter HuggingFace Token", key="chatbot_api_key", type="password")
    "[Get an Huggingface API key](https://huggingface.co/settings/tokens/new?tokenType=read)"
    model_name = st.selectbox(
        "Choose a model",
        [
            "mistralai/Mistral-7B-Instruct-v0.3",
            "mistralai/Mistral-7B-Instruct-v0.2",
            "HuggingFaceH4/zephyr-7b-beta",
            "meta-llama/Meta-Llama-3.1-8B-Instruct",
            "meta-llama/Meta-Llama-3.1-70B-Instruct"

        ],
        index=0  # default selected
    )


st.title("ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How Can I Assist You?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What are you looking for?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        if huggingface_api_key :
            try :
                assistant_response = bot(prompt, huggingface_api_key, model_name)
            except Exception as e:
                st.error(f"Error: {e}")
                assistant_response = "An error occurred. Please try again."
        else:
            assistant_response = "Please enter your Hugging Face API key to continue."

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "    
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    #
    st.session_state.messages.append({"role": "assistant", "content": full_response})