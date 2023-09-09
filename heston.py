import numpy as np
# import pandas as pd
from scipy.integrate import trapezoid
def heston_integrand(S, K, r, tau, kappa, theta, sigma, v_0, rho, u, b, phi):
    """
    S: underlying price
    K: strike price
    r: risk-free rate
    tau: time to maturity

    kappa: the mean reversion speed for the variance
    theta: the mean reversion level for the variance
    sigma: vol of vol
    v_0: initial level of variance
    rho: correlation between two Brownian motion

    u & b are PDE parameters
    phi relates the differential term.
    """
    x = np.log(S)
    a = kappa * theta
    d = np.sqrt(np.square(b - rho * 1j * sigma * phi)-np.square(sigma) * (2j * u * phi - np.square(phi)))
    root1 = b - rho * sigma * 1j * phi - d 
    root2 = root1 + 2 * d
    g = root2 / root1

    D = root2 / np.square(sigma) * ((1 - np.exp(d * tau)) / (1 - g * np.exp(d * tau)))
    C = r * 1j * phi * tau + a / np.square(sigma) * (root2 * tau - 2* np.log((1 - g * np.exp(d * tau))/(1 - g)))

    f = np.exp(C + D * v_0  + 1j*phi*x)
    y = np.exp(-1j * phi * np.log(K)) * f / 1j / phi
    return y.real

def heston_price(Is_call, S, K, r, tau, kappa, theta, sigma, v_0, rho, Lphi, Uphi, dphi):
    """
    call option price is 
        C(K) = S * Q^s(S_T>K) - K * exp(-r*tau) * Q(S_T>K)
    Q^s and Q are integrated, intergrand presents above.
    """
    phi = np.arange(Lphi, Uphi, dphi)
    int1 = []; int2 = []
    for i in phi:
        int1.append(heston_integrand(S,K, r, tau, kappa, theta, sigma, v_0, rho, 0.5, b = kappa + 0 - rho * sigma, phi = i))
        int2.append(heston_integrand(S,K, r, tau, kappa, theta, sigma, v_0, rho, -0.5, b = kappa + 0 , phi = i))
    I1 = trapezoid(int1, phi)
    I2 = trapezoid(int2, phi)
    P1 = 1/2 + 1/np.pi * I1
    P2 = 1/2 + 1/np.pi * I2
    call_price = S * P1 - K * np.exp(-r*tau) * P2
    
    if Is_call:
        return call_price
    else:
        put_price = call_price - S + K * np.exp(-r*tau)
        return put_price
        