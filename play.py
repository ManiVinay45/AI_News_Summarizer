import streamlit as st
import re

st.set_page_config(
    page_title="YouTube Player",
    page_icon="▶️",
    layout="centered"
)

st.title("▶️ YouTube Video Player")

youtube_url = st.text_input(
    "Enter YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

def get_video_id(url):
    patterns = [
        r"(?:youtube\.com/watch\?v=)([^&]+)",
        r"(?:youtu\.be/)([^?&]+)",
        r"(?:youtube\.com/embed/)([^?&]+)",
        r"(?:youtube\.com/shorts/)([^?&]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


if youtube_url:
    video_id = get_video_id(youtube_url)

    if video_id:
        st.success("YouTube video found!")

        st.video(
            f"https://www.youtube.com/watch?v={video_id}"
        )

    else:
        st.error("Invalid YouTube URL. Please enter a valid YouTube link.")