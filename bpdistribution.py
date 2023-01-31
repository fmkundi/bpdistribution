import math
### Binomial Distribution ###
class Binomial:
    """
    compute the probability of an event following Binomial distribution
    n:  the number of trials (occurrences)
    x:  the number of successful trials
    p:  probability of success in a single trial
    """
    param = 0
    def __init__(self):
        self.param = 0
    
    # probability density function
    def pdf(self,x,n,p):
        q=1-p
        e1 = n-x
        p = math.comb(n,x)*(p**x)*(q**e1)
        return(p)
    
    # cumulative distribution function
    def cdf(self,x,n,p,steps=False):
        tp = 0
        terms = {}
        q=1-p
        tt = x+1
        for x in range(tt):
            e1=n-x
            tp=tp+(p**x)*math.comb(n,x)*(q**e1)
            if(steps):
                terms[x]=(p**x)*math.comb(n,x)*(q**e1)
            
        if(steps):
            terms["Prob"]=tp
            return(terms)
        else:
            return(tp)

    # survival function
    def sf(self,x,n,p):
        return(1-self.cdf(x,n,p))
    
    # common statistics
    def stats(self,n,p):
        q=1-p
        mean = n*p
        med = math.floor(mean)
        mode = math.floor((n+1)*p)
        var = n*p*q
        skew = (q-p)/math.sqrt(n*p*q)
        kurt = (1-6*p*q)/(n*p*q)
        res = {"mean":mean,"median":med,"mode":mode,"variance":var,"skewnes":skew,"kurtosis":kurt}
        return(res)
### Poisson Distribution ###
class Poisson:
    """
    Compute the probability of an event following Poisson distribution.

    x:  value of random variable following Poisson distribution
    mu: the average number of times an event occurs
    """
    param = 0
    def __init__(self):
        self.param = 0
    
    # probability density function
    def pdf(self,x,mu):
        p = (math.exp(-mu) * (mu)**x)/math.factorial(x)
        return(p)
    
    # cumulative ditribution function
    def cdf(self,x,mu,steps=False):
        tp = 0
        terms ={}
        for x in range(x+1):
            p = (math.exp(-mu) * (mu)**x)/math.factorial(x) 
            if(steps):
                terms[x]=p
            tp = tp + p
        if(steps):
            terms["Prob"]=tp
            return(terms)
        else:
            return(tp)
    
    # survival function (1-cdf)
    def sf(self,x,mu):
        return(1-self.cdf(x,mu))
    
    # common statistics
    def stats(self,mu):
        mean = mu
        med = mu + 1/3-(1/(50*mu))
        mode = math.floor(mu)
        var = mu
        skew = 1/math.sqrt(mu)
        kurt = 1/mu
        res = {"mean":mean,"median":med,"mode":mode,"variance":var,"skewnes":skew,"kurtosis":kurt}
        return(res)
