import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Page Configuration ----------------
st.set_page_config(
    page_title="AI Employee Retention System",
    page_icon="👤",
    layout="centered"
)

#  Load Model ----------------
model = pickle.load(open("best_model_HR_1.pkl", "rb"))

st.title("👤 AI Employee Retention System")

st.markdown("""
### Predict Employee Attrition using Artificial Intelligence

This application predicts whether an employee is **likely to Stay** or **Leave**
the organization based on employee information.

Please fill in the employee details below and click **Predict**.
""")

st.divider()

#Input Section ----------------
with st.expander("📝 Employee Details", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        Age = st.number_input(
            "Age",
            min_value=18,
            max_value=70,
            value=35,
            help="Employee's current age in years."
        )

        JobLevel = st.selectbox(
            "Job Level",
            [1, 2, 3, 4, 5],
            index=1,
            help="1 = Entry Level, 5 = Senior Management."
        )

        MonthlyIncome = st.number_input(
            "Monthly Income",
            min_value=1000,
            value=5000,
            help="Employee's monthly salary."
        )

        TotalWorkingYears = st.number_input(
            "Total Working Years",
            min_value=0,
            value=8,
            help="Total years of work experience."
        )

        Department_str = st.selectbox(
            "Department",
            ["Human Resources", "Research & Development", "Sales"],
            index=2,
            help="Department where the employee works."
        )

        Gender_str = st.selectbox(
            "Gender",
            ["Female", "Male"],
            index=1
        )

        MaritalStatus_str = st.selectbox(
            "Marital Status",
            ["Divorced", "Married", "Single"],
            index=1
        )

    with col2:

        DistanceFromHome = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=100,
            value=10,
            help="Distance between home and office (km)."
        )

        PercentSalaryHike = st.number_input(
            "Salary Hike (%)",
            min_value=0,
            value=12,
            help="Latest salary hike percentage."
        )

        YearsAtCompany = st.number_input(
            "Years At Company",
            min_value=0,
            value=4,
            help="Number of years worked in this company."
        )

        BusinessTravel_str = st.selectbox(
            "Business Travel",
            ["Non-Travel", "Travel_Rarely", "Travel_Frequently"],
            index=1,
            help="Frequency of business travel."
        )

        EducationField_str = st.selectbox(
            "Education Field",
            ["Human Resources", "Life Sciences", "Marketing",
             "Medical", "Technical Degree", "Other"],
            index=3
        )

        JobRole_str = st.selectbox(
            "Job Role",
            ["Healthcare Representative",
             "Human Resources",
             "Laboratory Technician",
             "Manager",
             "Manufacturing Director",
             "Research Director",
             "Research Scientist",
             "Sales Executive",
             "Sales Representative"]
        )

        OverTime_str = st.selectbox(
            "OverTime",
            ["No", "Yes"],
            index=0,
            help="Does the employee regularly work overtime?"
        )

# Encoding ----------------

BusinessTravel = {
    "Non-Travel": 0,
    "Travel_Rarely": 1,
    "Travel_Frequently": 2
}[BusinessTravel_str]

Department = {
    "Human Resources": 0,
    "Research & Development": 1,
    "Sales": 2
}[Department_str]

EducationField = {
    "Human Resources": 0,
    "Life Sciences": 1,
    "Marketing": 2,
    "Medical": 3,
    "Technical Degree": 4,
    "Other": 5
}[EducationField_str]

Gender = {
    "Female": 0,
    "Male": 1
}[Gender_str]

JobRole = {
    "Healthcare Representative": 0,
    "Human Resources": 1,
    "Laboratory Technician": 2,
    "Manager": 3,
    "Manufacturing Director": 4,
    "Research Director": 5,
    "Research Scientist": 6,
    "Sales Executive": 7,
    "Sales Representative": 8
}[JobRole_str]

MaritalStatus = {
    "Divorced": 0,
    "Married": 1,
    "Single": 2
}[MaritalStatus_str]

OverTime = {
    "No": 0,
    "Yes": 1
}[OverTime_str]

st.markdown("<br>", unsafe_allow_html=True)

# Predict Button ----------------

if st.button("🔍 Predict Employee Retention", use_container_width=True):

    input_data = pd.DataFrame({
        "Age": [Age],
        "DistanceFromHome": [DistanceFromHome],
        "JobLevel": [JobLevel],
        "MonthlyIncome": [MonthlyIncome],
        "PercentSalaryHike": [PercentSalaryHike],
        "TotalWorkingYears": [TotalWorkingYears],
        "YearsAtCompany": [YearsAtCompany],
        "BusinessTravel": [BusinessTravel],
        "Department": [Department],
        "EducationField": [EducationField],
        "Gender": [Gender],
        "JobRole": [JobRole],
        "MaritalStatus": [MaritalStatus],
        "OverTime": [OverTime]
    })

    prediction = model.predict(input_data)

    st.divider()

    if prediction[0] == 1:
        st.error("⚠️ Employee is likely to Leave the Organization.")
    else:
        st.success("✅ Employee is likely to Stay in the Organization.")

#Footer ----------------

st.divider()
st.caption("🚀 Built with Deep Learning & Streamlit")
