def option_payoff(option_type, strike, premium, quantity, spot_prices):
    """
    Calcula o payoff de uma opção europeia.
    """
    if option_type == "Call":
        payoff = [(max(spot - strike, 0) - premium) * quantity for spot in spot_prices]
    elif option_type == "Put":
        payoff = [(max(strike - spot, 0) - premium) * quantity for spot in spot_prices]
    else:
        raise ValueError("Tipo inválido: use 'Call' ou 'Put'")
    return payoff

def total_payoff(options, spot_prices):
    """
    Soma os payoffs de várias opções.
    """
    total = [0] * len(spot_prices)
    individual = []

    for opt in options:
        payoff = option_payoff(
            opt["type"], opt["strike"], opt["premium"], opt["quantity"], spot_prices
        )
        individual.append(payoff)
        total = [t + p for t, p in zip(total, payoff)]

    return individual, total
