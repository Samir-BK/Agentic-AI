from urllib.parse import urlparse

import streamlit as st
from youtube_analyzer import build_yt_agent


st.set_page_config(

    page_title = "Youtube video analyzer",
    layout = "centered"
)

st.title("▶️ Analyze your YouTube video")
st.caption("Summarize videos, find key moments, or ask questions about the transcript.")

@st.cache_resource
def get_agent():
    return build_yt_agent()


agent = get_agent()


def is_youtube_url(value: str) -> bool:
    parsed_url = urlparse(value)
    return parsed_url.hostname in {"youtube.com", "www.youtube.com", "youtu.be"}


youtube_url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=...",
)
analysis_mode = st.radio(
    "Analysis type",
    ["Summary", "Key moments", "Ask a question"],
    horizontal=True,
)

question = ""
if analysis_mode == "Ask a question":
    question = st.text_input("Your question", placeholder="What is the main argument?")

submit_col, clear_col = st.columns(2)
with submit_col:
    submitted = st.button("Analyze", type="primary", use_container_width=True)
with clear_col:
    clear_result = st.button("Clear", use_container_width=True)

if clear_result:
    st.session_state.pop("analysis_result", None)

if submitted:
    clean_url = youtube_url.strip()
    if not clean_url:
        st.warning("Enter a YouTube URL to continue.")
    elif not is_youtube_url(clean_url):
        st.warning("Enter a valid YouTube URL.")
    elif analysis_mode == "Ask a question" and not question.strip():
        st.warning("Enter a question to continue.")
    else:
        prompts = {
            "Summary": "Summarize this YouTube video and identify its key points.",
            "Key moments": "Identify the key moments and include timestamps when available.",
            "Ask a question": f"Answer this question using the video transcript: {question.strip()}",
        }
        with st.spinner("Processing..."):
            response = agent.run(f"{prompts[analysis_mode]} Video URL: {clean_url}")
        st.session_state["analysis_result"] = response.content

if st.session_state.get("analysis_result"):
    st.divider()
    st.markdown(st.session_state["analysis_result"])