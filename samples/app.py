import streamlit as st
from colbot import qa_bot

st.title("RAG QA App with 🦜🔗 & 🦙")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Input your query here!!!"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.status("Running...") as status_bar:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = qa_bot(qry=question)
            full_response = response
            message_placeholder.markdown(full_response)
            status_bar.update(expanded=True, state="complete", label="Completed")
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
