from fastapi import FastAPI

from pydantic import BaseModel, Field

from src.predict import predict_churn

import pandas as pd
df = pd.read_csv("data/preprocessed/processed_data.csv")

app = FastAPI()

class CustomerData(BaseModel):

    tenure:int
    MonthlyCharges:float
    TotalCharges:float
    AvgMonthlySpend:float

    Contract_Month_to_month:int
    Contract_One_year:int

    OnlineSecurity_No:int
    OnlineBackup_No:int
    TechSupport_No:int

    InternetService_Fiber_optic:int
    InternetService_DSL:int

    PaymentMethod_Electronic_check:int

    PaperlessBilling_Yes:int

    Partner_Yes:int
    Dependents_Yes:int

    MultipleLines_Yes:int

    StreamingTV_Yes:int
    StreamingMovies_Yes:int

@app.get("/")
def show():
    return {
        "message": "Hello, welcome to my customer churn project api"
        }

@app.get("/about")
def about():
    return {"message": "I am Tash and this is my first end-to-end ML project."}

@app.get("/details")
def details():

    customerdata = df.head(5)

    return {
        "customers_example" : customerdata.to_dict(orient= "records")
        
    }

@app.post("/predict")
def predict(data: CustomerData):

    input_data = {

        "tenure":
        data.tenure,
        
        "MonthlyCharges":
        data.MonthlyCharges,

        "TotalCharges":
        data.TotalCharges,

        "AvgMonthlySpend":
        data.AvgMonthlySpend,

        "Contract_Month-to-month":
        data.Contract_Month_to_month,

        "Contract_One year":
        data.Contract_One_year,

        "OnlineSecurity_No":
        data.OnlineSecurity_No,

        "OnlineBackup_No":
        data.OnlineBackup_No,

        "TechSupport_No":
        data.TechSupport_No,

        "InternetService_Fiber optic":
        data.InternetService_Fiber_optic,

        "InternetService_DSL":
        data.InternetService_DSL,

        "PaymentMethod_Electronic check":
        data.PaymentMethod_Electronic_check,

        "PaperlessBilling_Yes":
        data.PaperlessBilling_Yes,

        "Partner_Yes":
        data.Partner_Yes,

        "Dependents_Yes":
        data.Dependents_Yes,

        "MultipleLines_Yes":
        data.MultipleLines_Yes,

        "StreamingTV_Yes":
        data.StreamingTV_Yes,

        "StreamingMovies_Yes":
        data.StreamingMovies_Yes

    }

    pred, prob = predict_churn(input_data)

    return {

        "prediction": int(pred),

        "probability": float(prob)

    }

