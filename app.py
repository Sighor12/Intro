import streamlit as st
from PIL import Image

st.title(" Mi Primear App en la Webb!!")

st.header("En este espacio comienzo a desarrollar mis apps para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('calavera con color.png')

st.image(image, caption='Interfaces multimodales')
