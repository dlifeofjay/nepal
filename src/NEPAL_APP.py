import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys

model = joblib.load('nepal.pkl')

st.title('Nepal Earthquake Prediction')
st.header('Input features')

st.subheader('Building Information')

age_building = st.number_input('Age of Building', min_value=0, max_value=999, value=10)
foundation_type = st.selectbox('Foundation Type', options=['Mud mortar-Stone/Brick', 'Cement-Stone/Brick', 'RC', 'Other', 'Bamboo/Timber'])
ground_floor_type = st.selectbox('Ground Floor Type', options=['Mud', 'Brick/Stone', 'RC', 'Timber', 'Other'])
height_ft_pre_eq = st.number_input('Height of Building (ft)', min_value=6, max_value=99, value=10)
land_surface_condition = st.selectbox('Land Surface Condition', options=['Flat', 'Moderate slope', 'Steep slope'])
other_floor_type = st.selectbox('Other Floor Type', options=['TImber/Bamboo-Mud', 'Timber-Planck', 'RCC/RB/RBC', 'Not applicable'])
plan_configuration = st.selectbox('Plan Configuration', options=['Rectangular', 'Square', 'L-shape', 'Multi-projected', 'Others','U-shape', 'T-shape', 'H-shape', 'E-shape','Building with Central Courtyard'])
plinth_area_sq_ft = st.number_input('Plinth Area (sq ft)', min_value=70, max_value=4995, value=1000)
position = st.selectbox('position', options=['Not attached', 'Attached-1 side', 'Attached-2 side', 'Attached-3 side'])
roof_type = st.selectbox('Roof Type', options=['Bamboo/Timber-Heavy roof', 'Bamboo/Timber-Light roof', 'RCC/RB/RBC'])
superstructure = st.selectbox('Superstructure', options=['mud_mortar_stone', 'cement_mortar_brick', 'rc_non_engineered', 'stone_flag', 'adobe_mud', 'mud_mortar_brick', 'timber', 'cement_mortar_stone', 'rc_engineered', 'bamboo', 'other'])

input_data = {
    'age_building': age_building,
    'foundation_type': foundation_type,
    'ground_floor_type': ground_floor_type,
    'height_ft_pre_eq': height_ft_pre_eq,
    'land_surface_condition': land_surface_condition,
    'other_floor_type': other_floor_type,
    'plan_configuration': plan_configuration,
    'plinth_area_sq_ft': plinth_area_sq_ft,
    'position': position,
    'roof_type': roof_type,
    'superstructure': superstructure
}

predictions = model.predict([input_data])

if st.button('Predict'):
    predictions = input_data
    if predictions == 1:
        st.error('The building is likely to be damaged in an earthquake.')
    else:
        st.success('The building is likely to be safe in an earthquake.')
else:
    st.info('Click the button to predict earthquake damage.')