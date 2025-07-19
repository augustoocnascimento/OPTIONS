# estrategias.py

def bull_call_spread():
    return [
        {"tipo": "Call", "strike": 100.0, "premio": 5.0, "long": True},
        {"tipo": "Call", "strike": 110.0, "premio": 2.0, "long": False},
    ]

def bear_put_spread():
    return [
        {"tipo": "Put", "strike": 110.0, "premio": 6.0, "long": True},
        {"tipo": "Put", "strike": 100.0, "premio": 3.0, "long": False},
    ]

def straddle():
    return [
        {"tipo": "Call", "strike": 100.0, "premio": 5.0, "long": True},
        {"tipo": "Put", "strike": 100.0, "premio": 5.0, "long": True},
    ]

def get_estrategias():
    return {
        "Bull Call Spread": bull_call_spread,
        "Bear Put Spread": bear_put_spread,
        "Straddle": straddle,
    }
