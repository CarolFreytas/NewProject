
import streamlit as st

st.write('Hello world!')

import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Exemplo 1

st.write('Hello, *World!* :sunglasses:')

# Exemplo 2

st.write(1234)

# Exemplo 3

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write(df)

# Exemplo 4

st.write('Abaixo está um quadro de dados:', df, 'Acima é um quadro de dados.')

# Exemplo 5

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Como você quer ser contactado?",
    ("Email", "Telefone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Escolha a frequencia",
        ("Padrão (5-15 dias)", "Express (2-5 dias)")
    )
