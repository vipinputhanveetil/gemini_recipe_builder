from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

#gemini call
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-2.0-flash')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize streamlit app
st.set_page_config(page_title="Gemini Recipe Builder")
st.header("Gemini Recipe Builder")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
submit=st.button("Gnerate Recipe")

## Button click
if submit: 
    response=get_gemini_response(input,image)
    st.subheader("The Response text:")
    st.write(response)
