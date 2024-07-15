import streamlit as st

st.title("Take Shot And Get An ID")

try:
    user_name = st.text_input("NAME")
    user_image = st.camera_input("Take A Shot")

    imageID = st.image(user_image, width=400, caption=f"{user_name}'s Image")
    nameID = st.header(user_name)
    st.write(f"""{user_name} is student at SMI ICT INSTITUTE""")
except AttributeError:
    st.info("Take a shot")
