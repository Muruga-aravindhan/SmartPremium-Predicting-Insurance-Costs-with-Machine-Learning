# SmartPremium-Predicting-Insurance-Costs-with-Machine-Learning
A machine learning project for predicting insurance premium costs using XGBoost, Random Forest, and Gradient Boosting models. Includes data preprocessing, feature engineering, model training, evaluation, and a Streamlit app for real-time premium prediction.

---

## Project Overview
Insurance premium pricing depends on multiple factors such as **age, income, health score, lifestyle, policy type, and claims history**.  
The goal of this project is to build a **predictive model** that estimates premium amounts accurately, helping insurers and customers make informed decisions.

---

## ⚙️ Features
- Data preprocessing & feature engineering
- Multiple ML models (XGBoost, Random Forest, Gradient Boosting)
- Trained **XGBoost model** exported as a `.pkl` file
- **Streamlit application** for interactive predictions
- Handles categorical encoding for user-friendly inputs

Usage

Open the Streamlit app in your browser.
Enter customer details such as age, gender, income, health score, lifestyle factors, and policy type.
Click Predict Premium Amount to get the estimated cost.

Models Used

XGBoost Regressor (best performing)
Random Forest Regressor
Gradient Boosting Regressor

Evaluation metrics:

R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)

Using MLflow

Reproducibility – track parameters, metrics, and datasets
Versioning – manage multiple versions of the model easily
Flexibility – The Streamlit app can always load the latest stable model
Transparency – complete experiment history is stored and viewable

Future Improvements

Add support for multiple models in the app (model selection dropdown)
Deploy Streamlit app on Streamlit Cloud / Heroku / AWS
Build an API with FastAPI / Flask
Expand the dataset with real-world insurance records

Aravindhan Manick
📧 Contact: aravindhanmanick@gmail.com
MCA Graduate | Data Science Enthusiast | ML Projects | Streamlit
