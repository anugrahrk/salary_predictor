import streamlit as st
import pickle
import numpy as np
def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data
data=load_model()
regressor_loaded=data["model"]
le_country=data["le_country"]
le_education=data["le_education"]
def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### Based on [StackOverFlow](https://survey.stackoverflow.co/2020) 2020 Survey""")
    countries=("United States","India","United Kingdom","Germany","Canada,Brazil","France","Spain","Australia","Netherlands","Poland","Italy","Russian Federation","Sweden")
    education=("Bachelor's degree","Master's degree","Less than a Bachelor's","Post grad")
    country=st.selectbox("Country",countries)
    education=st.selectbox("Country",education)
    experience=st.slider("Years of Experience",0,50,3)

    button=st.button("Calculate Salary")
    if button:
        x=np.array([[country,education,experience]])
        x[:,0]=le_country.transform(x[:,0])
        x[:,1]=le_education.transform(x[:,1])
        x=x.astype(float)
        salary=regressor_loaded.predict(x)
        st.subheader(f"The estimated salary is ${salary[0]:2f}")