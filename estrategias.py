# estrategias.py

def bull_call_spread(K1, K2, premium1, premium2):
    return [
        {"tipo": "Call", "strike": K1, "premio": premium1, "long": True},
        {"tipo": "Call", "strike": K2, "premio": premium2, "long": False}
    ]

def bear_put_spread(K1, K2, premium1, premium2):
    return [
        {"tipo": "Put", "strike": K1, "premio": premium1, "long": False},
        {"tipo": "Put", "strike": K2, "premio": premium2, "long": True}
    ]

def straddle(K, call_premium, put_premium):
    return [
        {"tipo": "Call", "strike": K, "premio": call_premium, "long": True},
        {"tipo": "Put", "strike": K, "premio": put_premium, "long": True}
    ]

def strangle(K1, K2, call_premium, put_premium):
    return [
        {"tipo": "Put", "strike": K1, "premio": put_premium, "long": True},
        {"tipo": "Call", "strike": K2, "premio": call_premium, "long": True}
    ]

def butterfly_call(K1, K2, K3, premium1, premium2, premium3):
    return [
        {"tipo": "Call", "strike": K1, "premio": premium1, "long": True},
        {"tipo": "Call", "strike": K2, "premio": premium2, "long": False},
        {"tipo": "Call", "strike": K3, "premio": premium3, "long": True}
    ]

def custom_strategy(legs):
    return legs
