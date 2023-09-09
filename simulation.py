import numpy as np
def gen_vol_sequence(kappa, theta, sigma,v_0, dt, tau):
    v = np.zeros(shape=int(tau//dt))
    v[0] = v_0
    for i in range(len(v) - 1):
        randomz = np.random.randn()
        v[i+1] = v[i] + kappa * (theta - v[i]) * dt
        v[i+1] += sigma * np.sqrt(v[i] * dt) * randomz
        v[i+1] += sigma**2 * (randomz**2 - 1) * dt / 4
    return v
def gen_und_sequence(v, rho, dt, tau):
    x = np.zeros(shape = int(tau / dt))
    for i in range(len(x) - 1):
        randomw = 