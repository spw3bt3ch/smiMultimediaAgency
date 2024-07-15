import streamlit as st

st.title("UI/UX Designs")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")
with col1:
    st.image("galleryImages/UI.png", caption="A Game App UI Design")
with col2:
    st.write("""UI (User Interface) and UX (User Experience) are two fundamental 
    aspects of designing digital products, such as websites and mobile applications. 
    While they are closely related, they focus on different elements of the user 
    interaction with a product.
    """)
    st.button("Send Us Your Design Brief")
