import re
import streamlit as st
import requests

WEBHOOKS_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY1MDYzZjA0MzA1MjY5NTUzNTUxMzMi_pc"


def email_validation(email):
    valid_email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(valid_email_pattern, email) is not None


st.title("Registration Form")
st.info("This is a pre-registration form which is meant to redirect to a payment before it can be successful")
with st.form("Coding Bootcamp Registration Form"):
    first_name = st.text_input("FIRST NAME")
    last_name = st.text_input("LAST NAME")
    phone = st.text_input("PHONE NUMBER")
    email_add = st.text_input("EMAIL ADDRESS")
    course = st.text_input("COURSE OF CHOICE")
    submit_button = st.form_submit_button('SUBMIT FORM')

# if submit_button:
#     st.success("Form submitted, proceed to Payment")

if not WEBHOOKS_URL:
    st.error("No email service presently")
    st.stop()

if not first_name:
    st.error("Fill in the missing field(s)")
    st.stop()

if not last_name:
    st.error("Fill in the missing field(s)")
    st.stop()

if not phone:
    st.error("Fill in the missing field(s)")
    st.stop()

if not email_add:
    st.error("Fill in the missing field(s)")
    st.stop()

if not course:
    st.error("Fill in the missing field(s)")
    st.stop()


data = {
    "First Name": first_name,
    "Last Name": last_name,
    "Phone Number": phone,
    "Email Address": email_add,
    "Course of Choice": course
}

response = requests.post(WEBHOOKS_URL, json=data)
if response.status_code == 200:
    st.success("Message sent successfully")
else:
    st.error("Message not sent, check connection or the email address")



