import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('webapp.py', 'rb'))

def medical_prediction(input_data):
    

    #changing input_data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data,dtype=np.float32)

    #reshaping the array
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print("The inasurence cost in USD")
    return prediction;
    
  
def main():
    #giving a title
    st.title('Medical Cost Prediction Web App')
    
    #getting the inout data from the user
    
    age=st.text_input('Age of person:')
    
    sex=st.text_input('Sex of person:')
    
    bmi=st.text_input('BMI of person:')
    
    children=st.text_input('Any childs?if any*:')
    
    smoker=st.text_input('Smoker or not:')
    
    region=st.text_input('Region of person:')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Cost Test Result'):
        diagnosis = medical_prediction([float(age),float(sex),float(bmi),float(children),float(smoker),float(region)])
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
