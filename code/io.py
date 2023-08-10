#!/usr/bin/env python3
import simulation
import optimisation
import time
import numpy as np
import plotly.express as px

def write_dataset(filename, X0 = 0, dX = simulation.increment_OU, steps = 10000):
    data = simulation.simulate_SDE(steps, X0, dX)
    np.array(data).tofile(f"../data/{filename}.np")

def read_dataset(filename):
    return np.fromfile(f"../data/{filename}.np")

def main():
    filename = 'ornstein_uhlenbeck_1691645968.112758'#f'ornstein_uhlenbeck_{time.time()}'
    #write_dataset(filename)
    prices = read_dataset(filename)

    #Train
    long_start_search_space = np.linspace(-min(prices), 0, 5)
    short_start_search_space = np.linspace(0, max(prices), 5)
    pnl, *params = optimisation.optimise(prices, long_start_search_space, short_start_search_space)
    print(f"{params=}")

    #Test (on training data)
    positions, pnls = optimisation.backtest(prices, *params)
    positions = np.array(positions,dtype=np.float64)

    results = pnl , pnls[-1] , np.dot(positions[:-1],np.diff(prices))
    for a in results:
        for b in results:
            assert abs(a-b) < 1e-12

    #Plot
    position_scale = np.max(np.abs(prices))
    data = np.array([positions[:-1] * position_scale, [pnls[0],*np.diff(pnls)], pnls, positions[:-1]*np.diff(prices), np.cumsum(positions[:-1]*np.diff(prices)), prices[:-1]]).T
    px.line(data).show()

if __name__ == "__main__":
    main()
