import streamlit as st
import requests
import sys
sys.path.append("../final_project")
from Entity import SentimentResult

# Define a Streamlit app
def streamlit_app():

    st.title("Emotion Detection App")

    text_to_analyze = st.text_area("Enter text to analyze:", "")
    if st.button("Analyze Emotion"):
        if text_to_analyze:
            # Make a request to the Flask backend
            response = requests.get("http://localhost:5000/emotionDetector", params={"textToAnalyze": text_to_analyze})         
            # Display the result
            st.subheader("Analysis Result:")
            st.write(f"{response.json()[0]} : {response.json()[1]}")
            
        else:
            st.warning("Please enter text to analyze.")
            
if __name__ == "__main__":
    streamlit_app()