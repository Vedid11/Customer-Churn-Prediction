# Customer Churn Prediction System

## Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning.

The project was built as an end-to-end ML system covering the complete workflow from preprocessing and model training to building an interactive prediction system using FastAPI and Streamlit.

---

## Problem Statement

Customer churn directly impacts business revenue. The objective of this project is to predict whether a customer is likely to churn based on customer information, billing details, contract type, and subscribed services.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit Learn
* XGBoost
* FastAPI
* Streamlit

---

## Project Structure

```text
Customer_Churn_p1/

├── app/
│   └── streamlit_app.py        # Streamlit frontend

├── backend/
│   └── main.py                 # FastAPI backend

├── data/
│   └── preprocessed/

├── images/                     # Saved plots/screenshots

├── models/
│   ├── churn_model.pkl
│   └── feature_columns.pkl

├── notebooks/
│   ├── churn_eda_preprocess.ipynb
│   └── model_training.ipynb

├── src/
│   └── predict.py              # Prediction pipeline

├── requirements.txt

└── README.md
```

---

## Project Workflow

### Data Preprocessing

* Data cleaning
* Missing value handling
* Encoding categorical variables
* Feature engineering
* Processed dataset generation

### Exploratory Data Analysis

Performed EDA to understand:

* Customer behavior
* Churn distribution
* Feature relationships

### Feature Engineering

Created additional features including:

* AvgMonthlySpend
* Customer tenure based features

### Model Training

Trained multiple models:

* Logistic Regression
* Random Forest
* XGBoost

### Handling Class Imbalance

Used:

**SMOTE (Synthetic Minority Oversampling)**

### Model Improvement

Performed:

* Cross Validation
* Hyperparameter Tuning using GridSearchCV

### Model Explainability

Used:

**SHAP**

to understand feature importance and model behavior.

### Deployment

Built:

* FastAPI backend for inference
* Streamlit frontend for predictions

---

## Running The Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Backend

```bash
python -m uvicorn backend.main:app --reload
```

### Run Streamlit Frontend

```bash
python -m streamlit run app/streamlit_app.py
```

---

## Future Improvements

* Cloud Deployment
* Better Feature Engineering
* Docker Support
* Monitoring and Logging
