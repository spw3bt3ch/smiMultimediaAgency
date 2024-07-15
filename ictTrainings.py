import streamlit as st

st.title("ICT Trainings")

st.image("galleryImages/codingSchool.png", caption="An Ongoing Registration")
st.link_button("Register For This Bootcamp Now", "https://forms.gle/u9DRjkjA7z9aXtu3A")
st.divider()

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")
with col1:
    st.image("galleryImages/Coding School Physical and Online classes.jpg", caption="Video Editing screen mode")
with col2:
    st.write("""ICT (Information and Communication Technology) training programs are 
    designed to improve skills in the use of technology for a variety of applications, 
    ranging from basic computer skills to advanced technical proficiencies. 
    These trainings are essential for both individuals and organizations to keep up 
    with the fast-paced developments in technology.
    
    Here are the courses we offer:
    1. Coding - (HTML5, CSS3, JavaScript, Python)
    2. Graphics Designs (CorelDraw, 
    Photoshop, Adobe Illustrator)
    3. Video Editing (Filmora)
    4. Digital Marketing
    5. Microsoft Office (Word, Excel, 
    Powerpoint, Access)
    """)

    st.link_button("Register for a course", "https://forms.gle/u9DRjkjA7z9aXtu3A", type="secondary")
