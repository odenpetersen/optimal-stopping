import numpy as np

def increment_OU(x, theta = 1, sigma = 1, dt = 0.01):
    dW = np.random.normal() 
    return dt * (sigma * dW - theta * x)

def simulate_SDE(steps, X0 = 0, dX = increment_OU):
    x = X0
    xs = [x]
    for _ in range(steps):
        x += dX(x)
        xs.append(x)
    return np.array(xs)
