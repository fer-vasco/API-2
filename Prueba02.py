import streamlit as st
from datetime import datetime

corrida = datetime.now()
current_time = corrida.strftime('%m-%d-%y %H:%M')

st.title('Resultados')
st.write(f'Datos actualizados el {corrida}')
