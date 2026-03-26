import numpy as np

def find_optimal(all_returns, all_vol, all_sharpe, all_weights):

    max_idx = np.argmax(all_sharpe)
    min_idx = np.argmin(all_vol)

    return {
        "max_sharpe": {
            "return": float(all_returns[max_idx]),
            "vol": float(all_vol[max_idx]),
            "weights": all_weights[max_idx].tolist()
        },
        "min_vol": {
            "return": float(all_returns[min_idx]),
            "vol": float(all_vol[min_idx]),
            "weights": all_weights[min_idx].tolist()
        }
    }