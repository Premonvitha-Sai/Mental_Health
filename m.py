import streamlit as st
import pandas as pd

# Assuming the dataset is a CSV file named 'dataset.csv'
@st.cache
def load_data():
    data = pd.read_csv('Mental_Health_FAQ.csv')
    return data

def main():
    data = load_data()

    st.title("Mental Health Question and Answer App")
    question = st.text_input('Please enter your question')

    if st.button('Search'):
        result = data[data['Questions'] == question]['Answers']
        if len(result) == 0:
            st.write("Sorry, we couldn't find an answer for your question.")
        else:
            st.write(result.values[0])

if __name__ == "__main__":
    main()
