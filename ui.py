import streamlit as st 
from youtube_analyzer import build_yt_agent


st.set_page_config(

    page_title = "Youtube video analyzer",
    layout = "centered"
)

st.title("▶️ Analyze your YouTube video")

@st.cache_resource
def get_agent():
    return build_yt_agent()


agent = get_agent()


youtube_url = st.text_input("YouTube URL")

if st.button("Submit"):
    if not youtube_url.strip():
        st.warning("Enter a YouTube URL to continue.")
    else:
        response = agent.run(
            f"Summarize this YouTube video and identify its key points: {youtube_url.strip()}"
        )
        st.markdown(response.content)