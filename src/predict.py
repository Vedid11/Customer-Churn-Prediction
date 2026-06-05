import pickle 
import pandas as pd
from pathlib import Path

 
with open(r"models\churn_model.pkl", "rb" ) as f:
    model= pickle.load(f)

with open(r"models\feature_columns.pkl" ,"rb") as f:
    feature_columns = pickle.load(f)

def predict_churn(input_dict):
    
    df= pd.DataFrame([input_dict])

    df= df.reindex(columns=feature_columns, fill_value=0)

    prediction= model.predict(df)[0]
    probability= model.predict_proba(df)[0][1]

    

    return prediction, probability
    