import streamlit as st
from page.payoff_page import render_payoff_page
from page.pricing_page import render_pricing_page


st.set_page_config(layout="wide")
st.title("Simulador de Opções - Menu Principal")

page = st.sidebar.selectbox("Escolha a página", ["Payoff Interativo", "Precificação de Opções"])

if page == "Payoff Interativo":
    render_payoff_page()
elif page == "Precificação de Opções":
    render_pricing_page()
