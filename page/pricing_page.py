import streamlit as st
import numpy as np
import plotly.graph_objects as go
from option_pricing import black_scholes_price, binomial_tree_price

def render_pricing_page():
    st.title("📈 Precificação de Opções")

    K = st.slider("Strike (K)", 50, 150, 100)
    T = st.slider("Tempo até vencimento (anos)", 0.01, 1.0, 0.5)
    r = st.number_input("Taxa livre de risco anual (%)", 0.0, 0.2, 0.05)
    sigma = st.number_input("Volatilidade anual (%)", 0.05, 0.8, 0.2)
    tipo = st.selectbox("Tipo da opção", ["call", "put"])

    S_values = np.linspace(0.5 * K, 1.5 * K, 200)

    bs_prices = [black_scholes_price(S, K, T, r, sigma, tipo) for S in S_values]
    bin_prices = [binomial_tree_price(S, K, T, r, sigma, tipo, steps=100) for S in S_values]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_values, y=bs_prices, mode='lines', name='Black-Scholes'))
    fig.add_trace(go.Scatter(x=S_values, y=bin_prices, mode='lines', name='Árvore Binomial'))

    fig.update_layout(
        title="Preço da Opção vs Preço do Ativo (Spot)",
        xaxis_title="Preço do Ativo (Spot)",
        yaxis_title="Preço da Opção",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
