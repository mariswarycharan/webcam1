import streamlit as st
from streamlit_webrtc import webrtc_streamer

def check_socket_connection():
    try:
        socket.create_connection(("localhost", 8080), 2)
        return True
    except socket.error:
        return False

b = st.button("check")
if b:
    st.code(check_socket_connection())
    

webrtc_ctx = webrtc_streamer(
    key="WYH")
