
import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from math import factorial
from scipy import stats


car_data = pd.read_csv('vehicles_us.csv', sep=',') 
#print (car_data)
dfhl = pd.read_csv('dfhl.xlsx')

st.header('Curso Data Science - Proyecto Individual Nro. 2: DATA ANALYTICS')

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

acusado_victima_button = st.button('Mostrar gráfico sunburst de acusados y víctimas')
if acusado_victima_button:
    df_sun = dfhl.groupby(['acusado', 'victima'])['n_victimas'].sum().reset_index()
    fig = px.sunburst(df_sun, path=['acusado', 'victima'], values='n_victimas', 
                  hover_data=['n_victimas'],  # Mostrar valores al pasar el mouse
                  title='Gráfico Sunburst con Valores de n_victimas')

fig.update_layout(width=800, height=600)
fig.show()