
import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Load the saved model, scaler, and PCA objects
with open('model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('pca.pkl', 'rb') as file:
    pca = pickle.load(file)

# Define the prediction function
def prediction(input_data):
    scaled_data = scaler.transform(input_data)
    pcs_data = pca.transform(scaled_data)
    pred = kmeans_model.predict(pcs_data)[0]

    if pred == 0:
        return 'Developed'
    elif pred == 1:
        return 'Developing'
    else:
        return 'Under Developed'

# Streamlit UI
def main():
    st.title('HELP INTERNATIONAL FOUNDATION')
    st.subheader('''This application helps classify a country based on its 
                    socio-economic and health factors''')

    # User inputs
    child_mor = st.text_input('Enter child mortality rate')
    lf_exp = st.text_input('Enter average life expectancy')
    tol_fer = st.text_input('Enter total fertility rate')
    health = st.text_input('Enter the % of GDP spent on health')
    export = st.text_input('Enter the % of GDP spent on exports')
    impor = st.text_input('Enter the % of GDP spent on imports')
    gdp = st.text_input('Enter GDP per Population')
    income = st.text_input('Enter the income per person')
    infl = st.text_input('Enter the inflation rate')

    if st.button('Predict'):
        try:
            # Convert inputs to float and arrange in correct order
            input_data = [[
                float(child_mor), float(export), float(health), float(impor),
                float(income), float(infl), float(lf_exp), float(tol_fer), float(gdp)
            ]]
            response = prediction(input_data)
            st.success(f'This country is: **{response}**')
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

if __name__ == '__main__':
    main()
