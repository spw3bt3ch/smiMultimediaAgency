import streamlit as st

st.title("Photo Speaks")

col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="bottom")
with col1:
    st.image("galleryImages/AI.jpg", caption="Python Programming")
    st.image("galleryImages/Helping God.png", caption="Public message")
with col2:
    st.image("galleryImages/H2H.png", caption="Graphics Design")
    st.image("galleryImages/H2H.png", caption="Graphics Design")
with col1:
    st.image("galleryImages/H2H.png", caption="Graphics Design")
    st.image("galleryImages/H2H.png", caption="Graphics Design")

