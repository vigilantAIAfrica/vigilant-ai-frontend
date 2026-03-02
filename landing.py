import streamlit as st

# 1. Page Configuration (The "Look")
st.set_page_config(page_title="Vigilant AI Africa", page_icon="🛡️", layout="centered")

# 2. Hero Section (The "Problem")
st.title("🛡️ Vigilant AI Africa")
st.subheader("Fighting the KES 2 Trillion Mobile Fraud Crisis")

st.markdown("""
Kenya lost over **KES 2 Trillion** to financial fraud in 2025. 
Vigilant AI is the digital shield protecting **Mama Mboga** and 
**Boda Boda riders** from AI-driven scams and SIM-swap tricks.
""")

# 3. The Personas (The "Why")
st.divider()
st.header("Who We Protect")
col1, col2 = st.columns(2)

with col1:
    st.info("### 🥬 Mama Mboga")
    st.write("**The Pain:** Lost KES 10,000 to a fake 'Wrong Number' reversal text.")
    st.write("**The Shield:** Our Swahili NLP flags the 'Urgent' tone instantly.")

with col2:
    st.success("### 🏍️ Juma (Boda Boda)")
    st.write("**The Pain:** Targeted by AI Voice Cloning scams pretending to be his boss.")
    st.write("**The Shield:** Real-time threat maps warn of high-risk callers.")

# 4. Milestone Progress (The "Proof")
st.sidebar.title("🚀 Phase 1: COMPLETE")
st.sidebar.markdown("""
- ✅ **Swahili NLP:** Translated 200M+ safety tips.
- ✅ **AI Scam Spotter:** 94% accuracy on DistilBERT.
- ✅ **Security Shield:** FastAPI Input Validation live.
- ✅ **SDG 8 Tracker:** KES impact tracked on Notion.
""")

# 5. Call to Action (The "Future")
st.divider()
st.write("### 📊 Our Real-World Impact")
st.write("Every scam we block saves an informal job. We are aligned with **UN SDG 8**.")

# Replace the link below with your actual Notion URL from earlier
st.link_button("View Live Impact Dashboard", "https://notion.so")

if st.button("Celebrate Phase 1 Completion!"):
    st.balloons()
    st.confetti() # This works if you have the streamlit-extras component
    st.write("Vigilant AI is now a shippable product. Great job, Charles!")
