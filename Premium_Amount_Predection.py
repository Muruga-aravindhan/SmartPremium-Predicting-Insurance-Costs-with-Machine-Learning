import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ==============================
# Load the trained model
# ==============================
with open("Insurance_Predection_XGBoost_model_new.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💰 Insurance Premium Prediction App")
st.write("Enter customer details to predict the insurance premium amount.")

# ==============================
# Collect user inputs (with exact categories from training)
# ==============================
age = st.number_input("Age", min_value=18, max_value=100, step=1)
gender = st.selectbox("Gender", ["Female", "Male","Transgender"])   # ✅ exact match
marital_status = st.selectbox("Marital Status", ["Married", "Divorced", "Single"])  # ✅ exact match
num_dependents = st.number_input("Number of Dependents", min_value=0, step=1)
education_level = st.selectbox("Education Level", ["Bachelor's Degree", "Master's Degree", "High School", "PhD"])  # ✅ exact match
occupation = st.selectbox("Occupation", ["Self-Employed", "Employed", "Unemployed"])  # ✅ exact match
health_score = st.slider("Health Score", 0, 100, 50)
location = st.selectbox("Location", ["Urban", "Rural", "Suburban"])  # ✅ exact match
policy_type = st.selectbox("Policy Type", ["Premium", "Comprehensive", "Basic"])  # ✅ exact match
previous_claims = st.number_input("Previous Claims", min_value=0, step=1)
vehicle_age = st.number_input("Vehicle Age (years)", min_value=0, step=1)
credit_score = st.slider("Credit Score", 300, 850, 600)
insurance_duration = st.number_input("Insurance Duration (years)", min_value=0, step=1)
customer_feedback = st.selectbox("Customer Feedback", ["Poor", "Average", "Good"])  # ✅ exact match
smoking_status = st.selectbox("Smoking Status", ["No", "Yes"])  # ✅ exact match
exercise_frequency = st.selectbox("Exercise Frequency", ["Weekly", "Monthly", "Daily", "Rarely"])  # ✅ exact match
property_type = st.selectbox("Property Type", ["House", "Apartment", "Condo"])  # ✅ exact match
policy_start_year = st.number_input("Policy Start Year", min_value=2000, max_value=2050, step=1)
policy_start_month = st.number_input("Policy Start Month", min_value=1, max_value=12, step=1)
policy_start_date = st.number_input("Policy Start Date", min_value=1, max_value=31, step=1)
annual_income = st.number_input("Annual Income", min_value=0.0, step=1000.0)

# ==============================
# Prepare input data
# ==============================
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender],
    'Marital Status': [marital_status],
    'Number of Dependents': [num_dependents],
    'Education Level': [education_level],
    'Occupation': [occupation],
    'Health Score': [health_score],
    'Location': [location],
    'Policy Type': [policy_type],
    'Previous Claims': [previous_claims],
    'Vehicle Age': [vehicle_age],
    'Credit Score': [credit_score],
    'Insurance Duration': [insurance_duration],
    'Customer Feedback': [customer_feedback],
    'Smoking Status': [smoking_status],
    'Exercise Frequency': [exercise_frequency],
    'Property Type': [property_type],
    'Policy_Start_Year': [policy_start_year],
    'Policy_Start_Date': [policy_start_date],
    'Policy_Start_Month': [policy_start_month],
    'Annual Income Normal': [annual_income]   # ✅ fixed column name
})

# ==============================
# Encode categorical variables
# ==============================
categorical_cols = [
    'Gender', 'Marital Status', 'Education Level', 'Occupation',
    'Location', 'Policy Type', 'Customer Feedback',
    'Smoking Status', 'Exercise Frequency', 'Property Type'
]

# Apply Label Encoding (⚠️ should ideally use saved encoders from training)
for col in categorical_cols:
    le = LabelEncoder()
    input_data[col] = le.fit_transform(input_data[col])

# ==============================
# Prediction
# ==============================
if st.button("Predict Premium Amount"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Predicted Premium Amount: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
