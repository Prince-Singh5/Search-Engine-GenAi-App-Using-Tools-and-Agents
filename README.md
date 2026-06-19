# 🔎 LangChain – Chat with Search

This project is a **Streamlit application** that integrates **LangChain agents** with multiple tools (Arxiv, Wikipedia, DuckDuckGo) and a **Groq LLM** backend.  
It allows you to ask questions in natural language and get answers powered by live search and research APIs, displayed in a conversational chat interface.

---

## 🚀 Features
- **Conversational UI** built with Streamlit’s `st.chat_message` and `st.chat_input`.
- **Groq LLM integration** (`llama-3.1-8b-instant`) for fast responses.
- **Search tools**:
  - [Arxiv](ca://s?q=Arxiv_tool_explanation) – fetches academic papers.
  - [Wikipedia](ca://s?q=Wikipedia_tool_explanation) – retrieves encyclopedia summaries.
  - [DuckDuckGo](ca://s?q=DuckDuckGo_tool_explanation) – searches the web.
- **Agent orchestration** using LangChain’s `initialize_agent` with `ZERO_SHOT_REACT_DESCRIPTION`.
- **Callback handler** (`StreamlitCallbackHandler`) to show the agent’s reasoning steps interactively.
- **Conversation memory** stored in `st.session_state`.

