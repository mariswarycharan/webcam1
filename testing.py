import streamlit as st
from streamlit_webrtc import webrtc_streamer

webrtc_ctx = webrtc_streamer(
    key="WYH")
