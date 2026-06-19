import streamlit as st
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from langchain_classic.agents import AgentType,initialize_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
load_dotenv()

## Arxiv and wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wikipedia_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wikepedia = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

## Tool to search from the internet
search = DuckDuckGoSearchRun(name="Search")

st.title("🔎 Langchain  - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
"""

## Side for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ API Key:",type="password")


# This code makes chatbot remember the conversation and show it on the screen.
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assisstant","content":"Hi, I am a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt := st.chat_input(placeholder="What is machine learning")  :
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(api_key=api_key,model="llama-3.1-8b-instant",streaming=True)
    tools = [wikepedia,search,arxiv]
    
    search_agent = initialize_agent(tools,llm,agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages,callbacks = [st_cb])
        st.session_state.messages.append({"role":'assisstane',"content": response})
        st.write(response)


