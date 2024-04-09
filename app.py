import os
import pickle
import streamlit as st

# Load the saved model
Airline_model = pickle.load(open('/Users/pdo/Downloads/Airline End to End/saved_model/Airline Passenger_model.sav', 'rb'))

# Assuming you have functions or dictionaries to encode categorical variables
# Example of a dictionary for label encoding (replace with your actual values)
gender_encoding = {'Male': 0, 'Female': 1}
customer_type_encoding = {'Returning': 0, 'First-time': 1}
type_of_travel_encoding = {'Personal': 0, 'Business': 1}
class_encoding = {'Economy': 0, 'Economy Plus': 1, 'Business': 2}

# Set page configuration
st.set_page_config(page_title="Airline Satisfaction",
                   layout="wide",
                   page_icon="✈️")

# Sidebar for navigation
st.sidebar.title("Navigation")
# You can add your sidebar navigation items here

# Main content
st.title('Airline Satisfaction Prediction using ML')

col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.selectbox('Gender', ['Male', 'Female'])

with col2:
    Age = st.number_input('Age', step=1,min_value=0)

with col3:
    CustomerType = st.selectbox('Customer Type', ['Returning', 'First-time'])

with col1:
    TypeOfTravel = st.selectbox('Type of Travel', ['Personal', 'Business'])

with col2:
    Class = st.selectbox('Class', ['Economy', 'Economy Plus', 'Business'])

with col3:
    FlightDistance = st.number_input('Flight Distance', step=1, min_value=0)

with col1:
    DepartureDelay = st.number_input('Departure Delay in Minutes', step=1, min_value=0)

with col2:
    ArrivalDelay = st.number_input('Arrival Delay in Minutes', step=1, min_value=0)

with col3:
    OnlineBoarding = st.slider('Online Boarding Rating', 1, 5)

with col1:
    InFlightService = st.slider('In-flight Service Rating', 1, 5)

with col2:
    InFlightWifiService = st.slider('In-flight Wifi Service Rating', 1, 5)
    
Airline_prediction = ''

# When predict button is clicked
if st.button('Predict Satisfaction'):

    # Encode the categorical data to match model training preprocessing
    Gender_encoded = gender_encoding[Gender]
    CustomerType_encoded = customer_type_encoding[CustomerType]
    TypeOfTravel_encoded = type_of_travel_encoding[TypeOfTravel]
    Class_encoded = class_encoding[Class]

    # Prepare user input for prediction, including encoded categorical variables
    user_input = [Gender_encoded, Age, CustomerType_encoded, TypeOfTravel_encoded, Class_encoded, FlightDistance,
                  DepartureDelay, ArrivalDelay, OnlineBoarding, InFlightService, InFlightWifiService]

    # Assuming user_input is ready for prediction after necessary preprocessing
    satisfaction_prediction = Airline_model.predict([user_input])

    # Displaying the prediction result
    if satisfaction_prediction[0] == 1:
       Airline_prediction = 'The passenger is Satisfied.'
    else:
        Airline_prediction = 'The passenger is Neutral or Dissatisfied.'
    st.success(Airline_prediction)

# Note: Ensure the preprocess function is defined or the necessary preprocessing steps are applied
# according to how the model was trained. The above code assumes categorical variables are handled accordingly.
