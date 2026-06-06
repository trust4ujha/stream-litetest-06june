import streamlit as st
from langchain_groq import ChatGroq

st.set_page_config(page_title='My AI Chat', layout='centered')

st.title("🤖 The Groq Chatbot")
st.write('A fully integrated, memory enabled AI Assistant')

# Sidebar API Key
with st.sidebar:
    st.header('⚙️ Configuration')
    user_api_key = st.text_input('Enter your Groq api key:', type='password')
    st.info('Your key is required to wake up the AI brain')

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Input
if user_query := st.chat_input('Message the AI....'):

    if not user_api_key:
        st.error('Please enter API Key in the sidebar first')
        st.stop()

    # Show user message
    with st.chat_message('user'):
        st.markdown(user_query)

    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )

    # LLM
    llm = ChatGroq(
        temperature=0.7,
        model="llama-3.3-70b-versatile",
        api_key=user_api_key
    )

    with st.spinner('AI is thinking....'):
        response = llm.invoke(st.session_state.messages)
        bot_answer = response.content

    # Bot message
    with st.chat_message('assistant'):
        st.markdown(bot_answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_answer}
    )
