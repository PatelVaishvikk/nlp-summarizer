import streamlit as st
from model import summarize, paraphrase

st.title("📝 Advanced Text Summarizer & Paraphraser")
st.write("Powered by T5-small (Summarization) & Pegasus (Paraphrasing)")

tab1, tab2 = st.tabs(["Summarize", "Paraphrase"])

with tab1:
    st.subheader("Text Summarization")
    input_text = st.text_area("Enter text to summarize:", height=200)
    if st.button("Summarize"):
        if input_text:
            with st.spinner("Generating summary..."):
                summary = summarize(input_text)
                st.success(summary)
        else:
            st.warning("Please enter some text!")

with tab2:
    st.subheader("Text Paraphrasing")
    input_text = st.text_area("Enter text to paraphrase:", height=200)
    if st.button("Paraphrase"):
        if input_text:
            with st.spinner("Generating paraphrases..."):
                paraphrases = paraphrase(input_text, num_return_sequences=2)
                for i, para in enumerate(paraphrases, 1):
                    st.write(f"Paraphrase {i}: {para}")
        else:
            st.warning("Please enter some text!")