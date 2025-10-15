import streamlit as st
import joblib
import numpy as np
st.title ("SALARY PREDCTION SASI APP")

st.divider()

st.write("with this app you can get estimators for company salariies of the company employee")
years = st.number_input("Enter the years at company",value=1, step= 1, min_value= 0)
jobrate = st.number_input("Enter the job Rating",value=1, step=1, min_value=0,max_value=5)
st.divider()
x = [years, jobrate] 

model = joblib.load("linear_model.pkl")

predict = st.button("press the button for salary prediction")
st.divider()


if predict:
    st.balloons()
    x1 = np.array([x])

    prediction = model.predict(x1)

    st.write(f"salary predction is a{prediction}")


else:

    "please press button for prediction"


