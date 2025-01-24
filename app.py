
import numpy as np
import pandas as pd
import streamlit as st
import pickle


# load all the instances that are required

with open('model.pkl','rb') as file:
    model=pickle.load(file)

with open('scaler.pkl','rb') as file:
    model=pickle.load(file)

with open('pca.pkl','rb') as file:
    model=pickle.load(file)


def prediction(input_data):
    scaled_data=scaler.transform(input_data)
    pcs_data=pca.transform(scaled_data)
    pred=model.predict(pca_data)[0]

    if pred==0:
        return 'Developed'
    elif pred==1:
        return 'Developing'
    else:
        return 'Under Developed'

def main():
    st.title('HELP INTERNATION FOUNDATION')
    st.subheader('''This application helps to classify the country on thr basis of its 
                 scio_economic and health factors''')
    child_mor=st.text_input('Enter child mortality rate')
    lf_exp=st.text_input('Enter average life expectancy')
    tol_fer=st.text_input('Enter total fertility rate')
    health=st.text_input('Enter the % of GDP spent on health')
    export=st.text_input('Enter the % of GDP spent on exports')
    impor=st.text_input('Enter the % of GDP spent on imports')
    gdp=st.text_input('Enter  GDP per Population')
    income=st.text_input('Enter the income per person')
    infl=st.text_input('Enter the inflation rate')

    input_data =[[child_mor,export,health,impor,income,infl,lf_exp,tol_fer,gdp]]

    if st.button('predict'):
        response=prediction(inp_list)
        st.success(response)

if __name__=='__main__':
    main()  
