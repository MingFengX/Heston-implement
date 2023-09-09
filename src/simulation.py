import numpy as np
def gen_sequence(r, kappa, theta, sigma,v_0,rho, dt, tau):
    v = np.zeros(shape=int(tau//dt))
    x = np.zeros(shape=int(tau//dt))
    v[0] = v_0
    for i in range(len(v) - 1):
        randomz = np.random.randn()
        randomw = np.random.randn() * np.sqrt(1 - rho**2) + rho * randomz
        v[i+1] = v[i] + kappa * (theta - v[i]) * dt
        v[i+1] += sigma * np.sqrt(v[i] * dt) * randomz
        v[i+1] += sigma**2 * (randomz**2 - 1) * dt / 4

        x[i+1] = x[i] + (r - v[i] /2) * dt
        x[i+1] += np.sqrt(v[i] * dt) * randomw
    return v, x
def gen_option_price(S, K, r, tau, kappa, theta, sigma, v_0, rho, dt, Nrepl):
    payoff = np.zeros(shape=Nrepl)
    und_price = np.zeros(shape=Nrepl)
    for i in range(Nrepl):
        v, x = gen_sequence(r, kappa, theta, sigma, v_0, rho, dt, tau)
        S_T = S * np.exp(x[-1])
        und_price[i] = S_T
        if S_T > K:
            payoff[i] = S_T - K
    payoff *= np.exp(-r * tau)
    call_option_price = np.sum(payoff)/Nrepl
    return und_price,payoff,call_option_price