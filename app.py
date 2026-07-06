import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Student Marks Analyzer", page_icon="📚")

st.title("📚 Student Marks Analyzer")
st.write("Enter marks to calculate total, average, percentage, and result.")

name = st.text_input("Student name")

maths = st.number_input("Maths marks", min_value=0, max_value=100, value=0)
physics = st.number_input("Physics marks", min_value=0, max_value=100, value=0)
chemistry = st.number_input("Chemistry marks", min_value=0, max_value=100, value=0)

if st.button("Calculate and Save"):
    if name.strip() == "":
        st.warning("Please enter the student name.")
    else:
        marks = np.array([maths, physics, chemistry])

        total = np.sum(marks)
        average = np.mean(marks)
        percentage = (total / 300) * 100

        if percentage >= 40:
            result = "Pass"
        else:
            result = "Fail"

        st.subheader("Result")
        st.write("Name:", name)
        st.write("Total:", total, "/ 300")
        st.write("Average:", round(average, 2))
        st.write("Percentage:", round(percentage, 2), "%")
        st.write("Result:", result)

        marks_df = pd.DataFrame({
            "Subject": ["Maths", "Physics", "Chemistry"],
            "Marks": [maths, physics, chemistry]
        })

        st.subheader("Marks Chart")
        st.bar_chart(marks_df.set_index("Subject"))

        new_data = pd.DataFrame([{
            "Name": name,
            "Maths": maths,
            "Physics": physics,
            "Chemistry": chemistry,
            "Total": total,
            "Average": round(average, 2),
            "Percentage": round(percentage, 2),
            "Result": result
        }])

        file_name = "student_records.csv"

        if os.path.exists(file_name):
            old_data = pd.read_csv(file_name)
            all_data = pd.concat([old_data, new_data], ignore_index=True)
        else:
            all_data = new_data

        all_data.to_csv(file_name, index=False)
        st.success("Student record saved successfully!")

st.divider()
st.subheader("All Student Records")

if os.path.exists("student_records.csv"):
    records = pd.read_csv("student_records.csv")
    st.dataframe(records)

    st.download_button(
        label="Download Student Records CSV",
        data=records.to_csv(index=False),
        file_name="student_records.csv",
        mime="text/csv"
    )
else:
    st.info("No student records saved yet.")