import streamlit as st
import numpy as np
import pickle
import pandas as pd


@st.cache_resource
def load_model():
    
    with open('trained_model2.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()


st.title("Mechanical Parts Pricing Prediction")


st.header("Mechanical Parts Details")
diameter = st.number_input("Enter Diameter (in inches):", min_value=0.0, step=0.1)
length = st.number_input("Enter Length (in inches):", min_value=0.0, step=0.1)


weight = np.pi * (diameter / 2) ** 2 * length * 0.286
st.write(f"Calculated Weight: {weight:.2f} lbs")

st.header("Material Details")

material_grade = st.selectbox(
    "Select Material Grade:", 
    ["F22", "4130"]
)

material_grade_value = {
    "F22":1,
    "4130": 1,
}[material_grade]

st.header("Add-Ons")
threading_type = st.selectbox("Select Threading Type Add-On:", ["VAM TOP®", "JFE Lion", "TenarisHydril Blue®"])
coating_addon = st.selectbox("Select Coating Add-On:", ["Phosphate", "Carbide", "Copper", "Xylan", "Nickel"])


threading_type_value = {"VAM TOP®":"VAM TOP®" , "JFE Lion": "JFE Lion", "TenarisHydril Blue®": "TenarisHydril Blue®"}[threading_type]
coating_addon_value = {"Phosphate": "Phosphate", "Carbide": "Carbide", "Copper": "Copper", "Xylan": "Xylan", "Nickel": "Nickel"}[coating_addon]


# Prediction
if st.button("Predict Price"):
    if diameter > 0 and length > 0:
        # Create a dataframe with input features
        input_data = pd.DataFrame({
            'Length (inches)': [length],
            'Weight (lbs)': [weight],  # Ensure `weight` is defined earlier in your code
            'Diameter (inches)': [diameter],
            'F22': [1 if material_grade == 'F22' else 0],
            '4130': [1 if material_grade == '4130' else 0],
            'JFE Lion': [1 if threading_type == 'JFE Lion' else 0],
            'TenarisHydril Blue®': [1 if threading_type == 'TenarisHydril Blue®' else 0],
            'VAM TOP®': [1 if threading_type == 'VAM TOP®' else 0],
            'Phosphating': [1 if coating_addon == 'Phosphating' else 0],
            'Xylan Coating': [1 if coating_addon == 'Xylan Coating' else 0],
            'Ni Plating': [1 if coating_addon == 'Ni Plating' else 0],
            'Cu Plating': [1 if coating_addon == 'Cu Plating' else 0],
            'Carbide Coating': [1 if coating_addon == 'Carbide Coating' else 0],
        })

        
       
        predicted_price = model.predict(input_data)[0]
        st.success(f"Predicted Price: ${predicted_price:.2f}")
    else:
        st.error("Please fill in all the inputs correctly.")
