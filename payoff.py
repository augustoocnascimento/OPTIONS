# payoff.py
import numpy as np

def call_payoff(S, K, premium, long=True):
    payoff = np.maximum(S - K, 0) - premium
    return payoff if long else -payoff

def put_payoff(S, K, premium, long=True):
    payoff = np.maximum(K - S, 0) - premium
    return payoff if long else -payoff

def total_payoff(S, legs):
    total = np.zeros_like(S)
    for leg in legs:
        tipo = leg["tipo"]
        strike = leg["strike"]
        premio = leg["premio"]
        long = leg["long"]

        if tipo == "Call":
            total += call_payoff(S, strike, premio, long)
        elif tipo == "Put":
            total += put_payoff(S, strike, premio, long)
    return total
