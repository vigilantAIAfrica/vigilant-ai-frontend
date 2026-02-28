import streamlit as st
from transformers import pipeline

# 1. Setup the Page Layout
st.set_page_config(page_title="Vigilant AI - Swahili Shield", page_icon="🛡️")

st.title("🛡️ Swahili Scam Translator")
st.write("Translate English scams to Swahili and understand the 'Red Flags'.")

# 2. Load the AI Model (Using a lightweight English-to-Swahili model)
# Note: On first run, this will download about 300MB.
@st.cache_resource
def load_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-sw")

translator = load_translator()

# 3. User Input
user_text = st.text_area("Paste the English scam message here:", 
                         placeholder="Example: Your account is locked. Click here to verify...")

if st.button("Analyze & Translate"):
    if user_text:
        # A. Perform Translation
        with st.spinner('Translating to Swahili...'):
            translation = translator(user_text)[0]['translation_text']
        
        st.subheader("🇰🇪 Swahili Translation:")
        st.success(translation)
        
        # B. Explain the "Red Flag" (The Rule-Based Logic)
        st.subheader("🚩 Why is this a Red Flag?")
        
        # Simple Logic to explain patterns
        if "click" in user_text.lower() or "http" in user_text.lower():
            st.warning("**Link Detected:** Legitimate banks rarely ask you to click links to 'verify' your account. This is a common Phishing tactic.")
        
        if "urgent" in user_text.lower() or "immediately" in user_text.lower():
            st.warning("**Urgency Detected:** Scammers use fear to make you act fast. Take a breath and call your bank directly.")
            
        st.info("**SDG 16 Impact:** By understanding this in your own language, you are protected from digital injustice.")
    else:
        st.error("Please paste some text first!")

st.sidebar.markdown("### Part of the Vigilant AI Shield")
st.sidebar.info("Building resilient infrastructure for Africa (SDG 9).")