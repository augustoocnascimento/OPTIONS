from datetime import datetime
from scipy.stats import norm
import numpy as np


def calculate_T(start_date, end_date):
    delta_days = (end_date - start_date).days
    return delta_days / 252  # considerando 252 dias úteis

def black_scholes_price(S, K, T, r, sigma, tipo='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if tipo == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price



def binomial_tree_price(S, K, T, r, sigma, tipo='call', steps=100):
    """
    Calcula o preço da opção usando o modelo binomial de CRR.
    """
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r*dt) - d) / (u - d)

    # Preços possíveis no vencimento
    ST = np.array([S * (u**j) * (d**(steps - j)) for j in range(steps + 1)])
    if tipo == 'call':
        payoff = np.maximum(0, ST - K)
    else:
        payoff = np.maximum(0, K - ST)

    # Backward induction
    for i in range(steps, 0, -1):
        payoff = np.exp(-r * dt) * (q * payoff[1:] + (1 - q) * payoff[:-1])
    return payoff[0]
