import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Ask questions and get AI-powered answers!")

api_key = st.text_input(
    "Enter your Gemini API Key:",
    type="password"
)

question = st.text_area(
    "Enter your question or topic:"
)

option = st.selectbox(
    "Choose an option:",
    ["Explain Topic", "Summarize", "Generate Quiz"]
)

if st.button("Generate Answer"):

    if not api_key:
        st.warning("Please enter your Gemini API Key.")

    elif not question:
        st.warning("Please enter a question.")

    else:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-1.5-flash")

        if option == "Explain Topic":
            prompt = f"Explain this topic in simple language: {question}"

        elif option == "Summarize":
            prompt = f"Give a short summary of: {question}"

        else:
            prompt = f"Create 5 MCQ questions with answers about: {question}"

        try:
            response = model.generate_content(prompt)

            st.subheader("AI Response")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
