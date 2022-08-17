# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:35:03 2022

@author: 91801
"""

import streamlit as st
import pickle
from streamlit_option_menu import option_menu

heartDisease_model = pickle.load(open('C:/Users/91801/Desktop/Prediction App/prediction_models/heartDiseaseModel.sav','rb'))
diabetes_model=pickle.load(open('C:/Users/91801/Desktop/Prediction App/prediction_models/Diabetes.sav','rb'))
breastCancer_pred_model=pickle.load(open('C:/Users/91801/Desktop/Prediction App/prediction_models/breastCancerPredictionModel.sav','rb'))
with st.sidebar: 
    
    
          selected=option_menu('Prediction System',
                        ['Heart Disease Prediction',
                          'Diabetes Prediction',
                          'Breast Cancer Classification',
                        'Health Insurance Prediction'],
                        default_index=0)
    
    
#Heart Disease Prediction Page 

if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using Machine Learning')
    
    col1, col2, col3 = st.columns(3)
        
    with col1:
            age= st.number_input('Enter your age')
            
    with col2:
            sex= st.number_input('Enter sex')
            
    with col3:
            cp= st.number_input('Chest pain type') 
        
    with col1:
            trestbps= st.number_input('Enter resting blood pressure')
              
    with col2:
            chol= st.number_input('Serum Cholestoral')
              
    with col3:
            fbs= st.number_input('Enter fasting blood sugar') 
              
    with col1:
            restecg= st.number_input('Enter rest ECG results')
              
    with col2:
            thalach= st.number_input('Maximum Heart Rate achieved')
              
    with col3:
            exang = st.number_input('Exercise Induced Angina')
              
    with col1:
            oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
            slope = st.number_input('Slope of the peak exercise ST segment')
            
    with col3:
            ca = st.number_input('Major vessels colored by flourosopy')
            
    with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
      
  
      
    heart_predi = ''
    
    if st.button('Heart Disease Predict'):
        heart_pred_result = heartDisease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                        
        
        if (heart_pred_result[0] == 1):
          heart_predi = 'THE PERSON HAS HEART DISEASE'
        else:
          heart_predi = 'THE PERSON DOES NOT HAVE HEART DISEASE'
        
    st.success(heart_predi)
        
    
#Diabetes prediction Page

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction Prediction using Machine Learning')
    
    col1, col2 = st.columns(2)
    with col1:
           Pregnancies = st.text_input('Number of Pregnancies')
            
    with col2:
            Glucose = st.text_input('Glucose Level')
            
    with col1:
           BloodPressure = st.text_input('Enter BloodPressure')
            
    with col2:
            SkinThickness = st.text_input('SkinThickness')
            
    with col1:
           Insulin = st.text_input('Insulin Level')
            
    with col2:
            BMI = st.text_input('BMI Level')
            
    with col1:
           DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction ')
            
    with col2:
            Age = st.text_input('Enter Age') 
     
          
     
        
    dia_prediction=''
     
    if st.button('Diabetes Predict'):
        diabetes_pred_result = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)]])                        
        
        if (diabetes_pred_result[0] == 1):
          dia_prediction = 'THE PERSON HAS DIABETES'
        else:
          dia_prediction = 'THE PERSON DOES NOT HAVE DIABETES'
        
    st.success(dia_prediction)
        

 # Breast Cancer Prediction Page

if (selected == 'Breast Cancer Classification'):
    
    # page title
    st.title('Breast Cancer Classification using Machine Learning')
    
    col1, col2, col3, col4 = st.columns(4)
        
    
    
    with col1:
            radius_mean= st.number_input('Enter radius_mean')
            
    with col2:
            texture_mean= st.number_input('Enter texture_mean')
            
    with col3:
            perimeter_mean= st.number_input('Enter perimeter_mean') 
        
    with col4:
            area_mean= st.number_input('Enter area_mean')
            
            
    
    with col1:
            smoothness_mean= st.number_input('Enter smoothness_mean')
            
    with col2:
            compactness_mean= st.number_input('Enter compactness_mean')
            
    with col3:
            concavity_mean= st.number_input('Enter concavity_mean') 
        
    with col4:
            concave_points_mean= st.number_input('Enter concave points_mean') 
            
            
            
              
    with col1:
            symmetry_mean= st.number_input('Enter symmetry_mean')
            
    with col2:
            fractal_dimension_mean= st.number_input('Enter fractal_dimension_mean')
            
    with col3:
            radius_se= st.number_input('Enter radius_se') 
        
    with col4:
            texture_se= st.number_input('Enter texture_se')
            
            
            
              
    with col1:
            perimeter_se= st.number_input('Enter perimeter_se')
            
    with col2:
            area_se= st.number_input('Enter area_se')
            
    with col3:
            smoothness_se= st.number_input('Enter smoothness_se') 
        
    with col4:
            compactness_se= st.number_input('Enter compactness_se')
            
            
            
    with col1:
            concavity_se= st.number_input('Enter concavity_se')
            
    with col2:
            concave_points_se= st.number_input('Enter concave points_se')
            
    with col3:
            symmetry_se= st.number_input('Enter symmetry_se') 
        
    with col4:
            fractal_dimension_se= st.number_input('Enter fractal_dimension_se')
            
            
            
    with col1:
            radius_worst= st.number_input('Enter radius_worst')
            
    with col2:
            texture_worst= st.number_input('Enter texture_worst')
            
    with col3:
            perimeter_worst= st.number_input('Enter perimeter_worst') 
        
    with col4:
            area_worst= st.number_input('Enter area_worst')
            
            
            
            
    with col1:
            smoothness_worst= st.number_input('Enter smoothness_worst')
            
    with col2:
            compactness_worst= st.number_input('Enter compactness_worst')
            
    with col3:
            concavity_worst= st.number_input('Enter concavity_worst') 
        
    with col4:
            concave_points_worst= st.number_input('Enter concave points_worst')
            
            
            
            
    with col1:
            symmetry_worst= st.number_input('Enter symmetry_worst')
            
    with col2:
            fractal_dimension_worst= st.number_input('Enter fractal_dimension_worst')
            
            
    
            
    bCancer_predi = ''
    
    if st.button('Breast Cancer Predict'):
        bcancer_pred_result = breastCancer_pred_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])                        
        
        if (bcancer_pred_result[0] == 1):
          bCancer_predi = 'THE BREAST CANCER IS BENIGN'
        else:
          bCancer_predi = 'THE BREAST CANCER IS MALIGNANT'
        
    st.success(bCancer_predi)
            
         




















if (selected == 'Health Insurance Prediction'):
    
    # page title
    st.title('Health Insurance Prediction using Machine Learning')    
    
    
    
    
    
    
    
