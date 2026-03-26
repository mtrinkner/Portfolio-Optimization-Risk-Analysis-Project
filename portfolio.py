import numpy as np

def generate_portfolios(returns):

    all_weights = []
    all_returns = []
    all_vol = []
    all_sharpe = []

    for i in range(21):
        for j in range(21):

            w1 = i / 20
            w2 = j / 20
            w3 = 1 - w1 - w2

            if w3 >= 0:
                weights = np.array([w1, w2, w3])

                portfolio_returns = returns.dot(weights)

                mean_return = portfolio_returns.mean()
                vol = portfolio_returns.std()
                sharpe = mean_return / vol

                all_weights.append(weights)
                all_returns.append(mean_return)
                all_vol.append(vol)
                all_sharpe.append(sharpe)

    return all_weights, all_returns, all_vol, all_sharpe