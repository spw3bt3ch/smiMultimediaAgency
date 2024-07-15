import streamlit as st

st.title("Graphics Designs")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")
with col1:
    st.image("galleryImages/Host movies poster modified.jpg", caption="One of our movie poster design")
with col2:
    st.write("""Graphic design is the art and practice of planning and 
    projecting ideas and experiences with visual and textual content. 
    It encompasses a variety of elements such as typography, imagery, 
    color, and layout to communicate a message or create a visual representation. 
    """)
    st.button("Send Us Your Design Brief")
