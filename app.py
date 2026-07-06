import streamlit as st
import pandas as pd
import numpy as np

# Page settings
st.set_page_config(
    page_title="Student Mark Analyzer",
    page_icon="📊",
    layout="centered"
)

# Custom design
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .title {
        text-align: center;
        color: #1f4e79;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #555555;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result-card {
        padding: 25px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📊 Student Mark Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Enter marks and get percentage, grade, and performance analysis.</div>',
    unsafe_allow_html=True
)

st.divider()

# Input section
st.subheader("📝 Enter Student Details")

name = st.text_input("Student Name", placeholder="Enter full name")

col1, col2, col3 = st.columns(3)

with col1:
    maths = st.number_input("Maths", min_value=0, max_value=100, value=0)

with col2:
    science = st.number_input("Science", min_value=0, max_value=100, value=0)

with col3:
    english = st.number_input("English", min_value=0, max_value=100, value=0)

st.write("")

if st.button("✨ Analyze Result", use_container_width=True):
    if name.strip() == "":
        st.warning("Please enter the student's name.")
    else:
        total = maths + science + english
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
            message = "Excellent performance! 🌟"
        elif percentage >= 80:
            grade = "A"
            message = "Very good performance! 👏"
        elif percentage >= 70:
            grade = "B"
            message = "Good work! Keep improving. 👍"
        elif percentage >= 60:
            grade = "C"
            message = "Nice effort. Practice more for better results. 📚"
        elif percentage >= 40:
            grade = "D"
            message = "You passed. Focus on improvement. 💪"
        else:
            grade = "F"
            message = "More practice is needed. You can improve! 📖"

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader(f"🎓 Result for {name}")

        a, b, c = st.columns(3)
        a.metric("Total Marks", f"{total}/300")
        b.metric("Percentage", f"{percentage:.2f}%")
        c.metric("Grade", grade)

        st.success(message)
        st.progress(int(percentage))
        st.markdown("</div>", unsafe_allow_html=True)

        chart_data = pd.DataFrame({
            "Subject": ["Maths", "Science", "English"],
            "Marks": [maths, science, english]
        }).set_index("Subject")

        st.subheader("📈 Subject-wise Performance")
        st.bar_chart(chart_data)
