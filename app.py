# Web Interface Development:- Web Application Deployment
import streamlit as st
import pickle
import datetime
from text_preprocessing import transform_text
from contact import contact_us

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Set page title and favicon
st.set_page_config(
    page_title="Spam Email Classification",
    page_icon="favicon.ico"
)

# Set page title
st.write('<div class="header">Spam Guard - Spam Email Classification</div>',
         unsafe_allow_html=True) # Error Handling

# Application Scaling and Performance Optimization
nav_selection = st.sidebar.radio(
    "Explore", ["Home", "Contact"])

# Add a clock component
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.markdown(f"{current_time}")

# Form Validation
if nav_selection == "Home":
    # Text input for user message
    input_sms = st.text_area("Enter the message")

    # Button to predict spam/ham
    if st.button('Predict'):
        # Input Preprocessing
        transformed_sms = transform_text(input_sms)

        # Vectorize input
        vector_input = tfidf.transform([transformed_sms])

        # Email Classification Prediction
        result = model.predict(vector_input)[0]

        # Result Display
        if result == 1:
            st.success("Spam Email")
        else:
            st.success("Not Spam Email")

elif nav_selection == "Contact":
    contact_us()

# Footer
st.markdown("---")
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# HTML and CSS Styling

st.write('<div class="footer">Made with ❤️ by Aniket Giri</div>',
         unsafe_allow_html=True)
