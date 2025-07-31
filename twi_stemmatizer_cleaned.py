import streamlit as st
import pandas as pd

# Original Twi words
twi_words = ['ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ', 'ɛyɛ', 'ɔdo', 'adwuma', 'nkwagyeɛ', 'ɛnoa', 'ɔba', 'ɛkɔ', 'ɔma', 'ɛtɔ', 'ɔwo', 'akoma', 'ɛdɔ', 'ɔfi', 'ɛbo', 'ɔsu', 'kɔkɔɔ', 'fitaa', 'ɛde', 'ɔman', 'nkɔsoɔ']

# Simple stemmatization logic (example: trim last 1-2 characters if length > 3)
def simple_stem(word):
    return word[:-2] if len(word) > 3 else word

# Apply stemming
stemmed_words = [simple_stem(word) for word in twi_words]

# Create dataframe
df = pd.DataFrame({
    "Original Word": twi_words,
    "Stemmed Word": stemmed_words
})

# Streamlit UI
st.title("Twi Stemmatization App")
st.write("This app processes 300 Twi words and shows their stemmed forms.")

# Display in a table
st.dataframe(df)
