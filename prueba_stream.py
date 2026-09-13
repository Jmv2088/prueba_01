import streamlit as st
import pandas as pd
import numpy as np

# Título
st.title("Mi primera aplicación Streamlit")

# Barra lateral
st.sidebar.header("Configuración")
st.sidebar.header("Otra")
st.sidebar.header("ESTA E OTRA")
st.sidebar.header("Config")


# Entrada de datos
nombre = st.text_input("¿Cómo te llamas?", "JULIAN")

if nombre:
    st.success(f"Hola!! {nombre}")

# Slider
num_puntos = st.slider(
    "Número de puntos",
    min_value=10,
    max_value=500,
    value=100
)

# Generar datos
datos = pd.DataFrame({
    "X": range(num_puntos),
    "Y": np.random.randn(num_puntos).cumsum()
})

# Mostrar datos
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(datos)

# Gráfica
st.line_chart(datos.set_index("X"))

# Botón
if st.button("Generar nuevos datos"):
    st.rerun()