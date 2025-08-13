import streamlit as st
import numpy as np
import plotly.graph_objects as go
from payoff import total_payoff



import streamlit as st

def render_payoff_page():
    st.header("Payoff Interativo")
    st.write("Esta é a página de payoff interativo.")


def render_payoff_page():
    st.title("📊 Estratégias com Opções – Payoff Interativo")

    # (aqui vai o código do seu payoff interativo)
    # Use sidebar, inputs, gráfico, tudo dentro desta função.
    spot_min = st.sidebar.number_input("Preço mínimo do ativo", value=0.0)
    spot_max = st.sidebar.number_input("Preço máximo do ativo", value=200.0)
    spot_prices = np.linspace(spot_min, spot_max, 300)

    num_options = st.sidebar.slider("Número de opções na estratégia", 1, 4, 2)

    options = []
    for i in range(num_options):
        st.sidebar.markdown(f"**Opção {i+1}**")
        option_type = st.sidebar.selectbox("Tipo", ["Call", "Put"], key=f"type_{i}")
        strike = st.sidebar.number_input("Strike", value=100.0, key=f"strike_{i}")
        premium = st.sidebar.number_input("Prêmio", value=5.0, key=f"premium_{i}")
        quantity = st.sidebar.number_input("Quantidade (positivo = comprado, negativo = vendido)", 
                                           value=1, step=1, key=f"quantity_{i}")
        options.append({
            "type": option_type,
            "strike": strike,
            "premium": premium,
            "quantity": quantity
        })

    individual, total = total_payoff(options, spot_prices)

    fig = go.Figure()
    for i, payoff in enumerate(individual):
        fig.add_trace(go.Scatter(
            x=spot_prices,
            y=payoff,
            mode='lines',
            name=f"Opção {i+1}",
            hovertemplate='Preço ativo: %{x:.2f}<br>Payoff: %{y:.2f}<extra></extra>'
        ))
    fig.add_trace(go.Scatter(
        x=spot_prices,
        y=total,
        mode='lines+markers',
        name="Payoff Total",
        line=dict(width=4, dash='dash'),
        hovertemplate='Preço ativo: %{x:.2f}<br>Total: %{y:.2f}<extra></extra>'
    ))
    fig.update_layout(
        title="Gráfico Interativo de Payoff",
        xaxis_title="Preço do Ativo na Data de Vencimento",
        yaxis_title="Payoff (R$)",
        hovermode="x unified",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
