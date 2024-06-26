import streamlit as st
from PIL import Image

st.title(" Mi Primera App en la Webb!!")

st.header("En este espacio comienzo a desarrollar mis apps para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('calavera con color.png')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Introduce texto', 'Texto propio')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Que modalidad es la principal de tu interfaz", ('visual', 'auditiva', 'Táctil'))
  if modo == 'visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de Botones")
if st.button('presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')
