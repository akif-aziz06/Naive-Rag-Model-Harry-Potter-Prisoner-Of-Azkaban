import os
import streamlit as st
import chromadb
from groq import Groq
from dotenv import load_dotenv

# 1. Setup and Initialization
load_dotenv()
st.set_page_config(page_title="Harry Potter RAG Explorer", page_icon="⚡")
st.title("⚡ Prisoner of Azkaban RAG Explorer")

# We use @st.cache_resource so Streamlit doesn't reconnect to the database on every click
@st.cache_resource
def init_db():
    chroma_client = chromadb.PersistentClient(path="./chroma_db_storage")
    return chroma_client.get_collection(name="harry_potter_rag")

collection = init_db()
client_groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Initialize Chat Memory
# This creates a blank list to store the conversation history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle New User Input
if user_query := st.chat_input("Ask a question about the book..."):
    
    # Show user's question on screen and save to memory
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Semantic Search / Retrieval
    results = collection.query(
        query_texts=[user_query],
        n_results=3  
    )
    
    # Combine the top 3 chunks into our context
    context = "\n".join(results['documents'][0])

    # Build Prompt
    rag_prompt = f"""
    CONTEXT: {context}

    QUERY: {user_query}

    Please generate a response according to the CONTEXT and QUERY. If the CONTEXT does not contain the answer, say 'I do not have this information'.
    """

    # Call Groq LLM
    with st.chat_message("assistant"):
        response = client_groq.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": rag_prompt}],
            max_tokens=200
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
    
    # Save AI's answer to memory so it stays on screen
    st.session_state.messages.append({"role": "assistant", "content": answer})