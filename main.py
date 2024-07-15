import streamlit as st

# ................................
# [theme]
# base="dark"
# backgroundColor="#020b20"
# ................................

# st.set_page_config(layout="centered")


st.markdown("""
<style>
.eyeqlp52.st-emotion-cache-1pbsqtx.ex0cdmw0
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

home = st.Page(
    page="about.py",
    title="Home",
    default=True
)

contact = st.Page(
    page="contact.py",
    title="Contact Us"
)

# gallery = st.Page(
#     page="gallery.py",
#     title="Photo Speaks"
# )

software = st.Page(
    page="softwareDev.py",
    title="Software Development"
)

web = st.Page(
    page="webDev.py",
    title="Website Development"
)

graphicsDesign = st.Page(
    page="graphicsdesign.py",
    title="Graphics Designs"
)

videoEdit = st.Page(
    page="VideoEditing.py",
    title="Video Editing"
)

productDesign = st.Page(
    page="productDesign.py",
    title="UI/UX Designs"
)

trainings = st.Page(
    page="ictTrainings.py",
    title="ICT Training"
)

cam = st.Page(
    page="cameraApp.py",
    title="Camera ID"
)

nav = st.navigation(
    {
        "ABOUT US": [home, contact],
        "SERVICES": [software, web, graphicsDesign, productDesign, videoEdit, trainings],
        "APPLICATION": [cam]
    }
)

st.sidebar.text("SMI Solutions || (c) 2024")
st.logo("smilogo.png")

nav.run()


