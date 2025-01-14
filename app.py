import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the trained model
@st.cache_resource
def load_model():
    # Replace 'trained_model.pkl' with the actual path to your saved model file
    with open('trained_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# App Title
st.title("Machine Parts Pricing Prediction")

# User Inputs
st.header("Machine Parts Details")
diameter = st.number_input("Enter Diameter (in inches):", min_value=0.0, step=0.1)
length = st.number_input("Enter Length (in inches):", min_value=0.0, step=0.1)

# Volume Calculation
volume = np.pi * (diameter / 2) ** 2 * length
st.write(f"Calculated Volume: {volume:.2f} cubic inches")

st.header("Material Details")
# Dropdown for Material Grade
material_grade = st.selectbox(
    "Select Material Grade ($/lb):", 
    ["Grade A", "Grade B", "Grade C", "Grade D"]
)

# Convert material grade to numeric values for prediction
material_grade_value = {
    "Grade A":12,
    "Grade B": 2.8,
    "Grade C": 3.5,
    "Grade D": 1.1
}[material_grade]

st.header("Add-Ons")
threading_type = st.selectbox("Select Threading Type Add-On (Beta):", ["VAM TOP®", "JFE Lion", "TenarisHydril Blue®"])
coating_addon = st.selectbox("Select Coating Add-On (Gamma):", ["Phosphate", "Carbide", "Copper", "Xylan", "Nickel"])
manufacturing_conversion = st.selectbox(
    "Select Manufacturing Conversion Factor (Alpha):", 
    ["X", "Y", "Z"]
)

# Convert threading, coating, and manufacturing conversion to numeric values for prediction
threading_type_value = {"VAM TOP®": 1.2, "JFE Lion": 1.15, "TenarisHydril Blue®": 1.17}[threading_type]
coating_addon_value = {"Phosphate": 1, "Carbide": 1.1, "Copper": 1.02, "Xylan": 1.01, "Nickel": 1.05}[coating_addon]
manufacturing_conversion_value = {
    "X": 1.8,
    "Y": 2.5,
    "Z": 4.2,
}[manufacturing_conversion]

# Prediction
if st.button("Predict Price"):
    if diameter > 0 and length > 0:
        # Create a dataframe with input features
        input_data = pd.DataFrame({
            'RM Cost/Lb': [material_grade_value],
            'Volume': [volume],
            'Alpha': [manufacturing_conversion_value],
            'Beta': [threading_type_value],
            'Gamma': [coating_addon_value]
        })
        
        # Predict using the model
        predicted_price = model.predict(input_data)[0]
        st.success(f"Predicted Valve Price: ${predicted_price:.2f}")
    else:
        st.error("Please fill in all the inputs correctly.")
