import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Ebuka's Website",
    page_icon="👋",
    layout="centered"
)

# Header
st.title("Welcome Ebuka")
st.subheader("Glad to have you here")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.write("This is your Streamlit website hosted with GitHub.")
    st.write("You can build pages, add charts, upload files, and more right from Python.")
    
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Nice to meet you, {name}!")
    
    if st.button("Click me"):
        st.balloons()

with col2:
    st.metric("Today", datetime.now().strftime("%B %d, %Y"))
    st.info("Built with Streamlit + GitHub")

# Footer
st.divider()
st.caption("Made by Ebuka | Deployed on Streamlit Community Cloud")