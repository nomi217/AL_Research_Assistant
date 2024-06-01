# Import libraries to build the app
import streamlit as st
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.arxiv_toolkit import ArxivToolkit
import os
from dotenv import load_dotenv
load_dotenv()


st.title("Chat with Arxiv 🔎🤖")
st.caption("This app allows you to chat with arXiv using OpenAI GPT-4o model.")

# Get OpenAI API key from .env file
openai_access_token = os.getenv("OPENAI_API_KEY")

if not openai_access_token:
    openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:

    assistant = Assistant(

        llm=OpenAIChat(
            model="gpt-4o-2024-05-13",
            max_tokens=1024,  
            temperature=0.9,  
            api_key=openai_access_token
        ),
        tools=[ArxivToolkit()],
        show_tool_calls=True
    )

    query = st.text_input("Enter your search about Arxiv")

    if st.button("Submit"):
        if query:
            response = assistant.run(query, stream=False)
            st.write(response)
        else:
            st.write("Please enter a query to search")
else:
    st.error("Error: Missing secret key! Please set up your .env file or enter the API key.")
