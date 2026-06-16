import streamlit as st
import requests

st.title(
    "Data GovIA"
)

st.write(
    "Intelligent Decision Support System for Data Governance and Data Management"
)

user_input = st.text_area(
    "Describe the organization",
    height=250
)

analyze_button = st.button(
    "Analyze"
)

if analyze_button:

    response = requests.post(

        "http://127.0.0.1:8000/analyze",

        json={
            "organization_description":
            user_input
        }

    )

    result = response.json()

    st.write(
        result
    )