import streamlit as st
from PIL import Image

st.title("Upload a File")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
