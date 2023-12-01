import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open('medicalcostwebapp.py'rb'))

def medical_prediction(input_data):
    try:
        # Ensure all input features are numeric
        input_data = [float(x) for x in input_data]

        # Reshape the input data
        input_data_reshaped = np.array(input_data).reshape(1, -1)

        # Make prediction
        prediction = loaded_model.predict(input_data_reshaped)
        return prediction[0]

    except ValueError:
        return "Error: Please provide valid numeric input for all features."


def main():
    # Giving a title
    st.title('Medical Cost Prediction Web App')

    # Getting the input data from the user
    age = st.text_input('Age of person:')
    sex = st.text_input('Sex of person:')
    bmi = st.text_input('BMI of person:')
    smoker = st.text_input('Smoker or not:')
    region = st.text_input('Region of person:')

    # Code for prediction
    cost = ''

    # Creating a button for prediction
    if st.button('Medical cost'):
        cost = medical_prediction([age, sex, bmi, smoker, region])

    st.write("The insurance cost in USD:", cost)


if __name__ == '__main__':
    main()
