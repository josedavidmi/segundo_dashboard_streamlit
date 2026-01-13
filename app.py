import streamlit as st 
import pandas as pd 
from streamlit_autorefresh import st_autorefresh
import time 

st.title("Dashboard en streaming desde un log CSV") 
# Refrescar cada 2000 milisegundos (2 segundos)
# key es importante para que el componente mantenga el estado
st_autorefresh(interval=2000, key="datarefresh")

# El resto de tu código (lectura de CSV y visualización)
df = pd.read_csv("https://raw.githubusercontent.com/josedavidmi/iabd-sbd/refs/heads/main/log_streamlit.log")
st.dataframe(df)
# Mostrar datos 
st.subheader("Últimos datos") 
st.dataframe(df.tail(2)) 
# Mostrar métricas 
#st.metric("Último valor", df["valor"].iloc[-1]) 
# Gráfico en tiempo real 
#st.line_chart(df["valor"]) 
