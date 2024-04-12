
import streamlit as st
import pandas as pd
import plotly_express as px

import numpy as np

import seaborn as sns

from matplotlib import pyplot as plt
from math import factorial
from scipy import stats


# df = pd.read_csv("Users/Juan/Documents/DataAnalytics/DA_S05_SoftwareDevelopment/DA_05_Project/vehicles_us.csv")

#car_data = pd.read_csv(
#   "vehicles_us.csv")
   # "/Users/Juan/Documents/DataAnalytics/DA_S05_SoftwareDevelopment/DA_05_Project/vehicles_us.csv")
car_data = pd.read_csv('vehicles_us.csv', sep=',') # leer los datos   
print (car_data)

st.header('Curso Data Analytics - Proyecto Sprint 05')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")  # crear un histograma
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir grafico de dispersion')

if scatter_button:
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    # mostrar un gráfico Plotly interactivo
    fig = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
