# bpdistribution
Binomial and Poisson Distribution from the Scratch
***Class Poisson***

**Method Summary**
| **Methods** |**Description**   |
| ------------ | ------------ |
|  **pdf(x,mu)** |Probability Density Function   |
|  **cdf(x,mu,steps=False)** |Cummulative Distribution Function   |
| **sf(x,mu)**  |Survival Function (1-cdf) |
|  **stats(mu)** | Mean, Median, Mode ,Variance, Skewness, Kurtosis   |
**Parameters**:
**x**: value of the poisson random variable. 
**mu**: average number of occurrences in specific interval.
**steps**: shows all probabilities from 0 to x when it is True.

***Class Binomial***

**Method Summary**
| **Methods**  |**Description**   |
| ------------ | ------------ |
| **pdf(x,n,p)**  |Probability Density Function   |
| **cdf(x,n,p,steps=False)**  | Cummulative Distribution Function  |
| **sf(x,n,p)**  | Survival Function (1-cdf)  |
| **stats(n,p)**  |Mean, Median, Mode ,Variance, Skewness, Kurtosis    |
**Parameters**:
**x**: value of the binomial random variable.
**n**: number of trials.
**p**: probability of success.
**steps**: shows all probabilities from 0 to x when it is True.
