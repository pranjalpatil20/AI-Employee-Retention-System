import streamlit as st
import numpy as np
import pandas as pd
import pickle 

# load model
model=pickle.load(open("best_model_HR_1.pkl", "rb"))

st.title("👤 AI Employee Retention System")

st.info("💡 Enter the employee's current age in years.")
Age = st.number_input("Age", min_value=18, max_value=70, value=35)

st.caption("Distance between the employee's home and workplace (in km).")
DistanceFromHome = st.number_input("DistanceFromHome", min_value=1, max_value=100, value=10)

JobLevel = st.selectbox("JobLevel", [1, 2, 3, 4, 5], index=1)

MonthlyIncome = st.number_input("MonthlyIncome", min_value=1000, value=5000)

PercentSalaryHike = st.number_input("PercentSalaryHike", min_value=0, value=12)

TotalWorkingYears = st.number_input("TotalWorkingYears", min_value=0, value=8)

YearsAtCompany = st.number_input("YearsAtCompany", min_value=0, value=4)

BusinessTravel_str = st.selectbox("BusinessTravel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"], index=1)

BusinessTravel_map = {"Non-Travel": 0, "Travel_Rarely": 1, "Travel_Frequently": 2}

BusinessTravel = BusinessTravel_map[BusinessTravel_str]


Department_str = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"], index=2)

Department_map = {"Human Resources": 0, "Research & Development": 1, "Sales": 2}

Department = Department_map[Department_str]


EducationField_str = st.selectbox("EducationField", ["Human Resources", "Life Sciences", "Marketing", "Medical", "Technical Degree", "Other"], index=3)

EducationField_map = {"Human Resources": 0, "Life Sciences": 1, "Marketing": 2, "Medical": 3, "Technical Degree": 4, "Other": 5}

EducationField = EducationField_map[EducationField_str]

Gender_str = st.selectbox("Gender", ["Female", "Male"], index=1)

Gender_map = {"Female": 0, "Male": 1}

Gender = Gender_map[Gender_str]


JobRole_str = st.selectbox("JobRole", ["Healthcare Representative", "Human Resources", "Laboratory Technician", "Manager", "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"], index=7)

JobRole_map = {
    "Healthcare Representative": 0, "Human Resources": 1, "Laboratory Technician": 2,
    "Manager": 3, "Manufacturing Director": 4, "Research Director": 5,
    "Research Scientist": 6, "Sales Executive": 7, "Sales Representative": 8
}
JobRole = JobRole_map[JobRole_str]

MaritalStatus_str = st.selectbox("MaritalStatus", ["Divorced", "Married", "Single"], index=1)

MaritalStatus_map = {"Divorced": 0, "Married": 1, "Single": 2}

MaritalStatus = MaritalStatus_map[MaritalStatus_str]

OverTime_str = st.selectbox("OverTime", ["No", "Yes"], index=0)

OverTime_map = {"No": 0, "Yes": 1}

OverTime = OverTime_map[OverTime_str]


if st.button("Predict"):
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
    
    st.write(input_data)
    
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("Employee is likely to Leave.")
    else:
        st.success("Employee is likely to Stay.")
