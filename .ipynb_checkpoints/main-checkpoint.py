from data import get_data
from portfolio import generate_portfolios
from optimize import find_optimal
from visualize import plot_frontier
from capm import compute_alpha_beta

import json
import pandas as pd

returns, market_returns = get_data()
weights, rets, vols, sharpes = generate_portfolios(returns)
best = find_optimal(rets, vols, sharpes, weights)

print("\nMAX SHARPE:")
print(best["max_sharpe"])

print("\nMIN VOL:")
print(best["min_vol"])

best_weights = best["max_sharpe"]["weights"]
portfolio_series = returns.dot(best_weights)

alpha, beta = compute_alpha_beta(portfolio_series, market_returns)

print("\nALPHA:", alpha)
print("BETA:", beta)

best["max_sharpe"]["alpha"] = float(alpha)
best["max_sharpe"]["beta"] = float(beta)

with open("web/results.json", "w") as f:
    json.dump(best, f, indent=4)

plot_frontier(rets, vols, sharpes)