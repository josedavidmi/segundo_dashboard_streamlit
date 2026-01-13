import streamlit as st 
import pandas as pd 
from streamlit_autorefresh import st_autorefresh
import time 

st.title("Dashboard en streaming desde un log CSV") 
# Refrescar cada 2000 milisegundos (2 segundos)
# key es importante para que el componente mantenga el estado
st_autorefresh(interval=2000, key="datarefresh")

# El resto de tu código (lectura de CSV y visualización)
df = pd.read_csv("tu_url_o_archivo.csv")
st.dataframe(df)
# Mostrar datos 
st.subheader("Últimos datos") 
st.dataframe(df.tail(10)) 
# Mostrar métricas 
st.metric("Último valor", df["valor"].iloc[-1]) 
# Gráfico en tiempo real 
st.line_chart(df["valor"]) 
# Esperar y refrescar 
time.sleep(2) 
st.experimental_rerun()