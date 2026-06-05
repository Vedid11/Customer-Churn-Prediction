import streamlit as st
import requests



st.set_page_config(

    page_title="Customer Churn Prediction",
    layout="wide"
)


st.title(
    "Customer Churn Prediction System"
)

st.write(
    "Predict whether a customer is likely to churn:"
)

st.sidebar.title("Customer Information")

col1,col2 = st.columns(2)


with col1:

    tenure = st.slider(

        "Tenure",0, 72, 24
    )

    monthly_charges = st.number_input(

        "Monthly Charges",0.0, 200.0, 70.0

    )

    total_charges = st.number_input(

        "Total Charges", 0.0, 10000.0, 1500.0

    )

    avg_monthly_spend = st.number_input(

        "Average Monthly Spend", 0.0, 500.0, 70.0

    )



with col2:

    contract = st.selectbox(

        "Contract",["Month-to-month", "One year"]

    )


    online_security = st.selectbox(

        "Online Security",["Yes","No"]

    )

    online_backup = st.selectbox(

        "Online Backup",["Yes","No"]

    )

    tech_support = st.selectbox(

        "Tech Support",["Yes","No"]

    )

    internet_service = st.selectbox(

        "Internet Service",["Fiber optic", "DSL"]

    )


paperless = st.selectbox(

    "Paperless Billing",["Yes","No"]

)

partner = st.selectbox(

    "Partner",["Yes","No"]

)

dependents = st.selectbox(

    "Dependents",["Yes","No"]

)

multiple_lines = st.selectbox(

    "Multiple Lines",["Yes","No"]

)

payment = st.selectbox(

    "Payment Method",["Electronic check", "Other"]

)

stream_tv = st.selectbox(

    "Streaming TV",["Yes","No"]

)

stream_movies = st.selectbox(

    "Streaming Movies",["Yes","No"]

)



if st.button("Predict Churn"):

    sample = {

        "tenure":tenure,

        "MonthlyCharges":monthly_charges,

        "TotalCharges":total_charges,

        "AvgMonthlySpend":avg_monthly_spend,

        "Contract_Month_to_month":

        int(contract=="Month-to-month"),

        "Contract_One_year":

        int(contract=="One year"),

        "OnlineSecurity_No":

        int(online_security=="No"),

        "OnlineBackup_No":

        int(online_backup=="No"),

        "TechSupport_No":

        int(tech_support=="No"),

        "InternetService_Fiber_optic":

        int(internet_service=="Fiber optic"),

        "InternetService_DSL":

        int(internet_service=="DSL"),

        "PaymentMethod_Electronic_check":

        int(payment=="Electronic check"),

        "PaperlessBilling_Yes":

        int(paperless=="Yes"),

        "Partner_Yes":

        int(partner=="Yes"),

        "Dependents_Yes":

        int(dependents=="Yes"),

        "MultipleLines_Yes":

        int(multiple_lines=="Yes"),

        "StreamingTV_Yes":

        int(stream_tv=="Yes"),

        "StreamingMovies_Yes":

        int(stream_movies=="Yes")

    }



    response = requests.post( "http://127.0.0.1:8000/predict", json=sample)

    result = response.json()

    pred = result["prediction"]

    prob = result["probability"]



    st.subheader("Prediction:")


    if pred==1:

        st.error(

            f"Customer likely to churn\n\nProbability: {prob:.2%}"

        )

    else:

        st.success(

            f"Customer unlikely to churn\n\nProbability: {prob:.2%}"

        )
        


    st.progress(
        float(prob)
    )