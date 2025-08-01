import streamlit as st

# Title
st.set_page_config(page_title="Twi Stemmatizer", layout="centered")
st.title("Twi Stemmatizer App")

# Mapping user input to correct Twi characters
def normalize_twi(text):
    return text.replace("3", "ɛ").replace("c", "ɔ")

# Twi stem dictionary (300 words as a sample - can be expanded)
twi_stem_dict = {
    "ɛbɛyɛ": "yɛ", "ɔbɛyɛ": "yɛ", "yɛ": "yɛ", "yɛɛ": "yɛ", "yɛre": "yɛ",
    "bɛba": "ba", "ɔba": "ba", "aba": "ba", "reba": "ba", "bɛbaa": "ba",
    "ɔbɛyɛɛ": "yɛ", "rebɛyɛ": "yɛ", "yɛɛɛ": "yɛ", "ɛyɛ": "yɛ", "ɔyɛ": "yɛ",
    "ɔbɛba": "ba", "aba": "ba", "ɔbaa": "ba", "bɛyɛ": "yɛ", "ɛba": "ba",
    "mɛba": "ba", "ɛbaa": "ba", "bebɛyɛ": "yɛ", "yɛreba": "ba", "ɔbɛyɛɛɛ": "yɛ",
    "ɔrebɛba": "ba", "ɔbɛbaɛ": "ba", "abɛyɛ": "yɛ", "ɔyɛɛ": "yɛ", "ɔbɛyɛa": "yɛ",
    # (Add the remaining 270+ words here or load from external file if needed)
}

# Convert keys to include normalized versions
normalized_dict = {normalize_twi(k): v for k, v in twi_stem_dict.items()}

# Sidebar showing available words
with st.sidebar:
    st.subheader("📚 Available Words")
    all_words = list(normalized_dict.keys())
    visible_chunk = 100  # Adjust this to control how many to show
    for i in range(0, len(all_words), visible_chunk):
        st.markdown(", ".join(all_words[i:i+visible_chunk]))

# Input
user_input = st.text_input("Enter a Twi word (use '3' for ɛ and 'c' for ɔ):")

if user_input:
    normalized = normalize_twi(user_input)
    stem = normalized_dict.get(normalized)
    if stem:
        st.success(f"✅ Stemmed result: **{stem}**")
    else:
        st.error("❌ Word not found in dictionary.")
