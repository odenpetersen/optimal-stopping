import itertools

def backtest(prices, long_start,short_start):
    pos = 0
    price_prev = prices[0]
    pnl = 0
    positions = [pos]
    pnls = []
    def sign(t):
        return 1 if t > 0 else -1 if t < 0 else 0
    for price in prices[1:]:
        pnl += pos * (price - price_prev)
        pnls.append(pnl)
        if sign(price_prev) == sign(pos):
            pos = 0
        if price_prev < long_start:
            pos = 1
        if price_prev > short_start:
            pos = -1
        positions.append(pos)
        price_prev = price
    return positions,pnls

#The search space is quadratic if both ranges are the same size. It could be linear with a smart refactor. A cartesian product is not required.
def optimise(prices, long_start_range, short_start_range):
    return max([(backtest(prices, *params)[1][-1], *params) for params in itertools.product(long_start_range, short_start_range)])
