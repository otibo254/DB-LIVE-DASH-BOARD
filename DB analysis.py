from logging import PlaceHolder
import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import csv


#Loading the dataset
df = pd.read_csv("C:/Users/stevi/Desktop/diabetes.csv")

#Setting page configurations
st.set_page_config(
    page_title="Live Dashboard.",
    page_icon="🎇",
    layout="wide"
)
st.caption("Breezie Foundation.")
#Setting page title
st.title("Live DB Analysis Board💫💫.")

#Creating filters
Outcome_filter = st.selectbox("Choose medical condition for analysis:",pd.unique(df['Outcome']))
st.write("###### 0: Represents Non Diabetic")
st.write("###### 1: Represents Diabetic")
st.write("###### Condition Selected:",Outcome_filter)

PlaceHolder = st.empty()

#Filtering job data to a unique selection
df = df[df['Outcome']==Outcome_filter]

for seconds in range(800):
    
    df['Insulin_new'] = df['Insulin'] * np.random.choice(range(1,6))
    df['BloodPressure_new'] = df['BloodPressure'] * np.random.choice(range(1,6))
    df['Glucose_new'] = df['Glucose'] * np.random.choice(range(1,6))
    df['SkinThickness_new'] = df['SkinThickness'] * np.random.choice(range(1,6))
    
    #KPI intergrations
    Insulin = np.mean(df['Insulin_new'])
    BloodPressure = np.mean(df['BloodPressure_new'])
    Glucose = np.mean(df['Glucose_new'])
    SkinThickness = np.mean(df['SkinThickness_new'])
    
    with PlaceHolder.container():
        KPIA,KPIB,KPIC,KPID = st.columns(4)
        KPIA.metric(label="Insulin🧪:", value=round(Insulin), delta=round(Insulin) -10)
        KPIB.metric(label="BloodPressure🩸:", value=round(BloodPressure), delta=round(BloodPressure) -10)
        KPIC.metric(label="Glucose💊:", value=round(Glucose), delta=round(Glucose) -10)
        KPID.metric(label="SkinThickness🧬:", value=round(SkinThickness), delta=round(SkinThickness) -10)
        
        #Creating charts and graphical displays
        graph1,graph2 = st.columns(2)
        with graph1:
            st.markdown(" ###### Heatmap:")
            graph1 = px.density_heatmap(data_frame=df, y='Age', x='Pregnancies')
            st.write(graph1)
            
        with graph2:
            st.markdown(" ###### Area Map:")
            graph2 = px.area(data_frame=df, y='Age', x='DiabetesPedigreeFunction')
            st.write(graph2)
            
        st.markdown("Tabular Display:")
        st.dataframe(df)
        time.sleep(1)