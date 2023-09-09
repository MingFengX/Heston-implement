# Heston-implement
 a report for implementing Heston model
 
 In this project, I try to implement the Heston model via standard inverse Fourier transform method showed in Heston(1993).

 I will simulate the same option price as well, left for comparison.

![Alt text](pic\price-time-series.png)
Above is simulated price time series, with parameters presented in Heston(1993). I change rho = 0.7 to show the rho effect. Please refer to src\heston.py for detailed parameter definition illustration.

![Alt text](pic\simulated-price-density.png)
Above is kerel density estimation, summarizing the simulated price time series. 
![Alt text](pic/vol-time-series.png)