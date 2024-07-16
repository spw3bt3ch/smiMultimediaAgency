import streamlit as st

# st.set_page_config(layout="centered")

st.markdown("""
<style>
.st-emotion-cache-15ecox0.ezrtsby0
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
# dev_image = st.image("galleryImages/Sam.png")
nav = st.navigation(
    {
        "ABOUT US": [home, contact],
        "SERVICES": [software, web, graphicsDesign, productDesign, videoEdit, trainings],
        "APPLICATION": [cam]
    }
)

st.sidebar.text("SMI Solutions || (c) 2024\n(Created using a Python framework)")
st.logo("galleryImages/smilogo.png")
# st.image("galleryImages/Sam.png")

nav.run()


