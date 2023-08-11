# Optimal Stopping
Find optimal parameters for position-limited long/short on a stationary, mean-reverting price series (e.g. Ornstein-Uhlenbeck).

![Example Plot](https://github.com/odenpetersen/optimal-stopping/blob/main/output/newplot.png?raw=true)

Technical note: in the case of a single Ornstein-Uhlenbeck bridge starting and ending at zero and taking positive values in between, I can't find a direct source for this, but based on the structure of the defining SDE, it should be a supermartingale, and so I think its Snell envelope is just itself. This means there actually is no uniquely optimal time to take on a position if all that matters is expected return.
However, we consider here not a single such bridge but a combination of bridges with varying durations. The heterogenous durations may have the consequence that there is an optimal threshold for expected-profit-per-unit-time. Taking transaction costs (e.g. spread) into account might also alter the dynamics.
Put differently: for a single short bet, this theoretical model says we should enter the position as soon as possible. However, because some bets pay off faster than others, this may not be a theoretically optimal strategy overall.
I'd need to have more of a think about this to figure out whether these considerations are actually significant.