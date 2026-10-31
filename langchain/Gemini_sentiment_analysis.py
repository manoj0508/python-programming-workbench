import streamlit as st
from google import genai


with open("Geminai_api_key.txt") as f:
    key = f.read().strip()
client = genai.Client(api_key=key)


st.title("Sentiment Analyzer")
review = st.text_area("Enter your review here")


if st.button("analyze"):
    if not review:
        st.write("Please enter the review")
    else :
        st.write("you entered : ")
        st.write(review)
        prompt = f"""
        Analyze the sentiment of the following review.


        Review:
        {review}


        Return exactly one word from the following options:
        Positive
        Negative
        Neutral


        do not provide any explanation.    
        """
        # response from model
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )
        sentiment = response.text.strip().lower()


        st.subheader("The sentiment for the review is  : ")
        st.write(f"Raw response from Gemini: {sentiment}")


        if sentiment == "positive":
            st.success(sentiment)
        elif sentiment == "negative":
            st.error(sentiment)
        else:
             st.info(sentiment)
