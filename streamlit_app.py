import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to process user input and generate a response
def process_input(user_input):
    doc = nlp(user_input)
    # Add your logic for generating a response based on user input
    # For simplicity, the chatbot just echoes the user input in this example
    response = "You said: " + user_input
    return response

# Streamlit app
def main():
    st.title("Simple Chatbot")

    # Text input for user to enter messages
    user_input = st.text_input("Enter your message:")

    if st.button("Send"):
        # Process user input and get response
        response = process_input(user_input)
        # Display response
        st.text("Bot: " + response)

if __name__ == "__main__":
    main()
