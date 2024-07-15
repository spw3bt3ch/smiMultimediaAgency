import streamlit as st

st.title("Video Editing")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")
with col1:
    st.image("galleryImages/ve.jpg", caption="Video Editing screen mode")
with col2:
    st.write("""Video editing is the post-production and arrangement of video shots. 
    To showcase perfect video editing to the public, video editors must be reasonable 
    and ensure they have a superior understanding of film, television, 
    and other sorts of videography.
    """)
    st.button("Send Us Your Video File to Edit")

