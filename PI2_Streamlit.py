import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import plotly.express as px
import plotly.graph_objects as go

#--------------------------------------------------------
dfhl = pd.read_excel('/Users/Juan/Documents/GitHub/DS_Project2/dfhl.xlsx')

#--------------------------------------------------------
st.title("Data Science. Proyecto Individual Nro. 2 - Análisis extra con gráficos de mayor complejidad")
st.markdown("***")

#--------------------------------------------------------
if st.checkbox("Ver dataset"):
    st.dataframe(dfhl)

#--------------------------------------------------------
if st.checkbox("Evolución de víctimas por comuna y periodo"):
    # Promedio mensual de víctimas por comuna
    df_period_comuna = dfhl.groupby(['aaaa', 'period', 'comuna', 'evento_tipo'])[['n_victimas']].sum().reset_index()
    df_period_comuna = df_period_comuna.sort_values(by='n_victimas', ascending=True)
    df_period_comuna['comuna'] = df_period_comuna['comuna'].astype('category')

    heat_pivot = df_period_comuna[df_period_comuna['aaaa'] >= 2019]
    heat_pivot = heat_pivot.pivot_table(index='comuna', columns='period', values='n_victimas', aggfunc='sum')

    fig = plt.figure(figsize=(14, 8))
    sns.heatmap(heat_pivot, cmap='YlGnBu')
    plt.title('Evolución de víctimas por comuna y periodo')
    plt.xlabel('Periodo')
    plt.ylabel('Comuna')
    st.pyplot(fig)

#--------------------------------------------------------
if st.checkbox("Cantidad y proporción acumulada de víctimas por comuna"):
   
    comunas_pareto = dfhl.groupby('comuna')['n_victimas'].sum().reset_index()
    comunas_pareto = comunas_pareto.sort_values(by='n_victimas', ascending=False)
    comunas_pareto['cum_victimas'] = comunas_pareto['n_victimas'].cumsum()
    comunas_pareto['cumperc_victimas'] = (comunas_pareto['n_victimas'].cumsum() / comunas_pareto['n_victimas'].sum()).round(2) * 100

    comunas_pareto['comuna'] = comunas_pareto['comuna'].astype(str) # Convertir el campo 'comuna' en una variable categórica
    comunas_pareto = comunas_pareto.sort_values(by='n_victimas', ascending=False)

    # Gráfico de Pareto
    fig, ax1 = plt.subplots(figsize=(14, 10))
    ax1.bar(comunas_pareto['comuna'], comunas_pareto['n_victimas'], color='lightblue')
    ax1.set_xlabel('Comuna')
    ax1.set_ylabel('Número de víctimas')
    ax1.tick_params('y')

    ax2 = ax1.twinx() # Eje Y secundario (porcentaje acumulado de víctimas)
    ax2.plot(comunas_pareto['comuna'], comunas_pareto['cumperc_victimas'], color='r', marker='o', linestyle='-')
    ax2.set_ylabel('Porcentaje acumulado de víctimas (%)', color='r')
    ax2.tick_params('y', colors='r')

    for i, perc in enumerate(comunas_pareto['cumperc_victimas']):
        ax2.annotate(f'{perc:.1f}%', (comunas_pareto['comuna'].iloc[i], perc), 
                    textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
        
    plt.title('Gráfico de Pareto: Número de víctimas por comuna')
    st.pyplot(fig)

#--------------------------------------------------------
if st.checkbox("Relación acusado-víctima - Cantidades"):
    # Dataset acusado-victima
    df_av = dfhl[['acusado', 'victima', 'evento_tipo', 'n_victimas']]
    pivot_av = df_av.pivot_table(index='victima', columns='acusado', values='n_victimas', aggfunc='sum', fill_value=0)

    colors = ["yellow", "orange", "red", "purple"]
    n_colors = len(colors)
    color_map = LinearSegmentedColormap.from_list("custom", colors, N=n_colors)

    fig = plt.figure(figsize=(14, 6))
    sns.heatmap(pivot_av, cmap=color_map, annot=True, fmt='d')

    plt.title('Ocurrencia de víctimas entre pares acusado-víctima', fontsize=14)
    plt.xlabel('Acusado', fontsize=12)
    plt.ylabel('Víctima', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

#--------------------------------------------------------
if st.checkbox("Relación acusado-víctima - Proporciones"):
    
    df_sun = dfhl.groupby(['acusado', 'victima'])['n_victimas'].sum().reset_index()
    custom_colors = px.colors.qualitative.Plotly

    # Crea el gráfico Sunburst y especifica los colores
    fig = px.sunburst(df_sun, path=['acusado', 'victima'], values='n_victimas', 
                    color='acusado',  # Utiliza la columna 'acusado' para definir los colores
                    color_discrete_sequence=custom_colors,  # Utiliza tus propios colores
                    hover_data=['n_victimas'],  
                    title='Gráfico Sunburst con Valores de n_victimas')

    fig.update_layout(width=800, height=600)
    fig.show()