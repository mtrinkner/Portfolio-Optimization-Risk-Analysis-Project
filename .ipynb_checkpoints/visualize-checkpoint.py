import matplotlib.pyplot as plt

def plot_frontier(all_returns, all_vol, all_sharpe):

    plt.figure()

    plt.scatter(all_vol, all_returns, c=all_sharpe)

    plt.xlabel("Volatility")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")

    plt.colorbar(label="Sharpe Ratio")
    plt.savefig("web/frontier.png")

    plt.show()