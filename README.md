# DS_Project2

Escuela: Soy Henry
Curso: Data Science Part Time, cohorte 7
Proyecto: Proyecto Individual 1, Data Analysis
Estudiante: Juan GARATE

El presente trabajo constituye el segundo de los proyectos individuales a presentar como parte de los requisitos para alcanzar la graduación del curso. El objetivo de este proyecto es la creación de un dashboard para el análisis de datos, en particular para datos de tráfico de la ciudad de Buenos Aires, Argentina durante los años 2016 a 2019.

El trabajo tiene como objetivo un desarrollo profesional con un enfoque académico ya que el EDA contienen comentarios en los pasos realizados, en función de que sea sencilla su corrección y pueda ser de utilidad a futuros estudiantes de data science.

El alcance del trabajo consta de dos fases: 1) el análisis de datos, y 2) presentación de resultados. No se considera como parte de este trabajo las recomendaciones que puede dar un especialista en accidentes viales en función de mejorar los indicadores. El análisis de datos se ha realizado en Python v3.12, mientras que la presentación de resultados se ha realizado en Microsoft Power BI. Es importante mencionar que la fase 1 se enfoca en entender el panorama general de los datasets provistos, así como de crear métricas que permitan al lector un entendimiento situacional. Por otro lado, si bien la fase 2 también tiene métricas, esta se enfoca en la visualización de los KPIs o indicadores claves de procesos. 

# Fases y contenidos:

## Fase 1: Análisis de datos (EDA):
* Importación de librerías y carga de datos
* Preprocesamiento de datos
    * Verificación de tipo de datos
    * Verificación de duplicados
    * Verificación de nulos
* Análisis de datos 
    * Estadística descriptiva
    * Serie de tiempo, tendencias y estacionalidad
    * Relación entre tipos de eventos    
    * Localizaciones
    * Tipos de víctimas
* Conclusiones

## Fase 2: Presentación de Resultados (DASHBOARD):
* Home: presentación general
* KPI1: Tasa semestral de siniestros
* KPI2: Cantidad anual de siniestros por moto
* KPI2: Cantidad anual de siniestros peatonales en comunas top5
* Serie temporal de eventos
* Estacionalidad: visualización de patrones
* Promedios mensuales históricos de lesiones y muertes
* Comunas: registro histórico y evolución
* Mapa interactivo: comunas de la ciudad de Buenos Aires
* Víctimas: principales grupos de víctimas y causantes


# Hallazgos y conclusiones:
Los registros históricos muestran, para toda la ciudad:
* Un promedio de 120 víctimas mortales por año
* Un promedio de 9200 víctimas lesionadas por año

Las series de tiempo muestran:
* Un promedio mensual de 10 víctimas mortales
* Un promedio mensual de 767 víctimas lesionadas
* En el año 2020 se registran abruptamente menos eventos, debido a la cuarentena del covid19
* Hay una tendencia a la baja en los últimos años, muy posiblemente vinculada al item anterior pues los datos están entre 2016-2021
* En cuanto a las estacionalidades:
    * Entre Octubre-Marzo se registran la mayor cantidad de eventos
    * Los fines de semana tienen menos actividad
    * El horario pico de accidentes se dá entre las 4 pm y 5 pm

El análisis entre tipos de eventos permite ver:
* Las lesiones y muertes tienen cierta correlatividad levemente positiva, lo cual es esperable
* Una gran cantidad de lesiones no necesariamente conlleva a un número alto de muertes

Del análisis geográfico, podemos determinar:
* Las comunas 1, 15 y 14 tienen los mayores promedios mensuales
* Las comunas 1, 15 y 4 tienen las mayores variabilidades
* Todas las comunas presentan una baja en el año 2020, lo cual indica que la aplicación de cuarentena fué global
* Las comunas 1 y 15 registran la mayor actividad de eventos, pero la comuna 15 ha ido disminuyendo sus accidentes
* El 50% de los eventos ocurren en sólo 6 comunas: la 1, 15, 4, 9, 3 y 14

El análisis de víctimas nos permite concluir en lo siguiente:
* Los autos son los principales causantes de accidentes
* Las motos son las principales víctimas
* Hay un total de 2468 (el 25% de los eventos) correspondientes al par auto-moto, en donde el accidente es ocasionado por el auto y la víctima es la moto
