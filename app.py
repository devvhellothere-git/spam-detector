import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 Spam SMS Detector")
message = st.text_area("Paste any SMS message here")

if st.button("Check"):
    result = model.predict(vectorizer.transform([message]))[0]
    if result == "spam":
        st.error("🚨 SPAM Detected!")
    else:
        st.success("✅ Not Spam")