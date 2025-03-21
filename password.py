import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon='🔐')

st.title('🔐Password Strength Meter')
st.markdown("## 🤝Welcome to the Password Strength Meter")

password = st.text_input("Enter your password", type='password')

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should have at least 8 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[A-Z]', password):
        score+=1
    else:
        feedback.append("❌Password should contain at least one uppercase letter.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one number.")

    if re.search(r'[!@#$%^&*()]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character (!@#$%^&*()).")
        score += 1
    if score == 4:
        feedback.append("✅Your Password is strong!🎉")
    elif score == 3:
        feedback.append("🟡Your Password is moderately strong!")
    else: 
        feedback.append("🔴Your Password is weak! Please try to make it stronger.")

    if feedback:
        st.markdown("## 🔒Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("🤖Please enter a password.")
