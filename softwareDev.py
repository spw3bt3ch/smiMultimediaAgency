import streamlit as st

st.title("Our Software Development")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")
with col1:
    st.image("galleryImages/savflex.jpg", caption="A screenshot of one of the Desktop App meant for Designers "
                                                  "and Printers")
with col2:
    st.write("""Software development is the process of creating, 
    designing, deploying, and supporting software. 
    It encompasses a variety of activities and methodologies, 
    from writing and testing code to understanding user requirements 
    and maintaining software after it has been deployed.
    """)
    st.button("Order a Software")


