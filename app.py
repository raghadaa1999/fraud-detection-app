import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="AI Fraud Detection", layout="wide")

st.title("Hybrid AI-Based Financial Fraud Detection")
st.write("This system uses a Machine Learning model to detect suspicious financial transactions.")

# Simple training dataset
data = pd.DataFrame({
    "amount": [100, 250, 500, 900, 1200, 3000, 4500, 6000, 7500, 9000, 12000, 15000],
    "transactions_today": [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "merchant_type": ["Online", "Restaurant", "Shopping", "Online", "Restaurant", "Shopping",
                      "ATM", "Transfer", "ATM", "Transfer", "Transfer", "ATM"],
    "is_fraud": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

encoder = LabelEncoder()
data["merchant_encoded"] = encoder.fit_transform(data["merchant_type"])

X = data[["amount", "transactions_today", "merchant_encoded"]]
y = data["is_fraud"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

st.header("Transaction Input")

amount = st.number_input("Transaction Amount", min_value=0.0)
transactions_today = st.number_input("Number of Transactions Today", min_value=0, step=1)
merchant_type = st.selectbox("Merchant Type", ["Online", "Restaurant", "Shopping", "ATM", "Transfer"])

if st.button("Detect Fraud"):
    merchant_encoded = encoder.transform([merchant_type])[0]

    new_transaction = pd.DataFrame({
        "amount": [amount],
        "transactions_today": [transactions_today],
        "merchant_encoded": [merchant_encoded]
    })

    prediction = model.predict(new_transaction)[0]
    probability = model.predict_proba(new_transaction)[0][1]
    risk_score = round(probability * 100, 2)

    st.header("Detection Result")
    st.write(f"Risk Score: {risk_score}%")

    if prediction == 1:
        st.error("🚨 Suspicious Transaction")
        st.write("Alert Status: Generated")
    else:
        st.success("✅ Normal Transaction")
        st.write("Alert Status: No Alert")

st.divider()

st.header("Analyst Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", "1200")
col2.metric("Suspicious Transactions", "87")
col3.metric("Normal Transactions", "1113")
   
