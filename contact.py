import streamlit as st

try:
    st.title("Contact Us")

    col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")
    with col1:
        st.write("""### Office Address:
        Location 1:
        105, Olambe Road,
        Olambe, Ogun state,
        Nigeria.
        
        Location 2:
        112, Iju Road,
        Agege, Lagos,
        Nigeria.
        
        +2347077705842
        www.smi.com.ng
        enquiry@smi.com.ng
        """)

    with col2:
        st.write("""### Send Us a Mail""")
        st.form(
            st.text_input("NAME"),
            st.text_input("EMAIL ADDRESS"),
            st.text_area("MESSAGE"),
            # st.form_submit_button("SEND MAIL", clear_on_submit=False, border=True)
        )
except TypeError:
    st.info("Fill-in your information correctly")

