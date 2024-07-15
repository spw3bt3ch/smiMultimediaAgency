import streamlit as st

st.title("Web Development")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")
with col1:
    st.image("galleryImages/web.png", caption="A screenshot of one a Website developed by us")
with col2:
    st.write("""Web development involves creating websites and web applications for the internet or an intranet. It encompasses various disciplines and skills 
    Creating a website is crucial for individuals and businesses alike for several reasons.
    """)
    st.button("Get A website")
