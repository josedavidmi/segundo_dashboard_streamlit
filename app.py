import streamlit as st 
import pandas as pd 
10 
import time 
st.title("Dashboard en streaming desde un log CSV") 
# Refrescar cada 2 segundos 
st_autorefresh = st.experimental_rerun 
# Leer el archivo CSV 
df = pd.read_csv("https://raw.githubusercontent.com/josedavidmi/iabd-sbd/refs/heads/main/log_streamlit.log") 
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