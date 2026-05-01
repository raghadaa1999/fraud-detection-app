import streamlit as st
import random

st.set_page_config(page_title="Fraud Detection", layout="wide")

st.title("Hybrid AI-Based Financial Fraud Detection")

amount = st.number_input("Transaction Amount", min_value=0.0)
time = st.text_input("Transaction Time (e.g. 22:30)")
location = st.text_input("Location")
merchant = st.selectbox("Merchant Type", ["Online", "ATM", "Transfer", "Restaurant"])
transactions = st.number_input("Transactions Today", min_value=0)

if st.button("Detect Fraud"):
    risk = 0

    if amount > 5000:
        risk += 30
    if transactions > 5:
        risk += 25
    if merchant in ["ATM", "Transfer"]:
        risk += 20
    if "22" in time or "23" in time:
        risk += 15

    risk += random.randint(5, 10)

    st.write("Risk Score:", risk)

    if risk >= 70:
        st.error("🚨 Suspicious Transaction")
    else:
        st.success("✅ Normal Transaction")
