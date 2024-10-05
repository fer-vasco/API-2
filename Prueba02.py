import streamlit as st
from datetime import datetime
import pandas as pd

corrida = datetime.now()
corrida = corrida.strftime('%m-%d-%y %H:%M')

st.title('Resultados')
st.write(f'Datos actualizados el {corrida}')

d = {'col1': [1, 2], 'col2': [3, 4], 'col3': [3, 4], 'col4': [3, 4], 'col5': [3, 4]}
df = pd.DataFrame(data=d)
st.dataframe(df)
