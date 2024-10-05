import streamlit as st
from datetime import datetime

corrida = datetime.now()

st.title('Resultados')
st.write(f'Datos actualizados el {corrida}')
