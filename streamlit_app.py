import streamlit as st
from story_generator import generate_story
st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("📚 AI Story Generator")
st.subheader("Generate a story with IBM watsonx.ai")
user_prompt = st.text_area("Enter your story prompt:", height=150)
if st.button("Generate Story"):
    if not user_prompt.strip():
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Generating your story..."):
            story = generate_story(user_prompt)
        st.success("Here's your AI-generated story:")
        st.text_area("Generated Story", story, height=400)
