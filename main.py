# streamlit run main.py
import streamlit as st
import pickle
import time
import cleantext

st.title("Amazon Review Sentiment Prediction")
with st.expander("Predict Text"):
    # Load model
    model = pickle.load(open('review_sentiment.pkl', 'rb'))

    # Predict text sentiment
    text = st.text_input("Type here: ")

    submit = st.button("Predict")

    if submit:
        start = time.time()
        prediction = model.predict([text])
        end = time.time()
        st.write("Prediction time taken: ", round(end-start, 4), "seconds")
        print(prediction[0])
        st.write("Predicted Sentiment is: ", prediction[0])

    # Return clean text
    pre_text = st.text_input("Clean Text: ")
    if pre_text:
        st.write(cleantext.clean(pre_text, clean_all=False, extra_spaces=True,
                                 stopwords=True, lowercase=True, numbers=True, punct=True))