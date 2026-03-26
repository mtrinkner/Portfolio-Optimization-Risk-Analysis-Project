import statsmodels.api as sm

def compute_alpha_beta(portfolio_returns, market_returns):

    X = sm.add_constant(market_returns)
    model = sm.OLS(portfolio_returns, X).fit()
    alpha = model.params['const']     
    beta = model.params[market_returns.name]  
    
    return alpha, beta