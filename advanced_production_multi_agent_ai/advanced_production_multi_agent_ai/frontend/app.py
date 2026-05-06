import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🚀 Production Multi-Agent AI System")

task = st.text_area("Enter Task")

if st.button("Run AI Agents"):
    response = requests.post(
        "http://127.0.0.1:8000/run-task",
        json={"task": task}
    )

    data = response.json()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Planner Agent")
        st.json(data["plan"])

    with col2:
        st.subheader("Executor Agent")
        st.json(data["execution"])

    with col3:
        st.subheader("Critic Agent")
        st.json(data["review"])

    st.success(f"Memory Entries: {data['memory_size']}")
