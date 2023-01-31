from bpdistribution import Binomial, Poisson

# Binomial
bp = Binomial()
x = 3
n = 10
p = 0.7
# P(X=3)
print(bp.pdf(x,n,p))   # 0.009001692000000007
# P(X<=3)
print(bp.cdf(x,n,p))   # 0.010592078400000008
# P(X>3)
print(1-bp.cdf(x,n,p)) # 0.9894079216

# Poisson
pp = Poisson()
x = 3
mu = 7
# P(X=3)
print(pp.pdf(x,mu))    # 0.052129252364199845
# P(X<=3)
print(pp.cdf(x,mu))    # 0.08176541624472163
# P(X>3)
print(1-pp.cdf(x,mu))  # 0.9182345837552783 


