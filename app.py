import streamlit as st
import pickle

# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit app
st.title('Email Spam Classifier')

# User input
message = st.text_area("Enter the email message here:")

if st.button('Classify'):
    if message:
        # Preprocess and transform the input message
        transformed_message = vectorizer.transform([message])
        prediction = model.predict(transformed_message)[0]

        if prediction == 1:
            result = "SPAM"
        else:
            result = "HAM"

        st.write(f'This email is classified as: **{result}**')
    else:
        st.write("Please enter a message to classify.")
