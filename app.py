# app.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from payoff import total_payoff

# Deve vir no topo!
st.set_page_config(page_title="Simulador de Estratégias com Opções", layout="centered")
st.title("📈 Visualizador de Estratégias com Opções")

st.sidebar.header("📌 Configuração da Estratégia")

# Define número de pernas (limitado a 2 no MVP)
num_legs = st.sidebar.selectbox("Número de pernas (legs)", [1, 2], index=1)

legs = []
for i in range(num_legs):
    st.sidebar.subheader(f"Perna {i+1}")
    tipo = st.sidebar.selectbox(f"Tipo de opção {i+1}", ["Call", "Put"])
    long = st.sidebar.radio(f"Posição {i+1}", ["Long", "Short"]) == "Long"
    strike = st.sidebar.number_input(f"Strike {i+1}", min_value=0.0, value=100.0 + i*10)
    premio = st.sidebar.number_input(f"Prêmio {i+1}", min_value=0.0, value=5.0)

    legs.append({
        "tipo": tipo,
        "strike": strike,
        "premio": premio,
        "long": long
    })

# Preços simulados do ativo
S = np.linspace(0.5 * min([leg["strike"] for leg in legs]),
                1.5 * max([leg["strike"] for leg in legs]), 300)

payoff = total_payoff(S, legs)

# Gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=S, y=payoff, mode='lines', name='Payoff líquido', line=dict(width=3)))
fig.update_layout(title="Gráfico de Payoff da Estratégia",
                  xaxis_title="Preço do ativo no vencimento",
                  yaxis_title="Lucro / Prejuízo",
                  template="plotly_white")

st.plotly_chart(fig, use_container_width=True)
