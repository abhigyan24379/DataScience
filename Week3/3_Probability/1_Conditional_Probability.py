import numpy as np
import matplotlib.pyplot as plt



# Bayes Theorem 

def bayes_theorem(priop , likelihood,evidence):
    return (likelihood * priop )/ evidence


# Common Probability distribution
# - Gaussian (Normal) Distribution 
#   -> Bell Shaped Curve with mean(meu) and standard deviation (sigma)

mu, sigma = 0,1
x = np.linspace(-4 , 4, 100 )
y = (1 / (np.sqrt(2 *np.pi * sigma**2))) * np.exp(-0.5 * ((x -mu) / sigma)**2)

# plt.plot(x,y)
# plt.title("Gaussian Distribution")
# plt.show()

# Bernoulli Distribution 
# - Describe outcomes of a binary experiment
#       p(x = 1) = p , p(x = 0) = 1 -p

# p = 0.6
# plt.bar([0,1],[1-p ,p], color ="Blue")
# plt.title("Bernaulli Distribution ")
# plt.xticks([0,1] , labels=["0 (Failure)", "1 (Success)"])
# plt.show()

# binomial distribution 
# P(X=k) = C(n, k) * pk * (1-p)(n-k)

# from scipy.stats import binom

# n , p = 10 , 0.5
# x = np.arange(0, n + 1)
# y = binom.pmf(x, n, p)
# plt.bar(x, y , color= "green")
# plt.show()


# Poisson Distribution 
# models the number of events in a fixed interval of time or space 
#  formula : -  P(X = k) = (e^(-λ) * λ^k) / k! 
from scipy.stats import poisson
lam = 3
x = np.arange(0,10)
y = poisson.pmf(x, lam)
plt.bar(x, y , color="Green")
plt.title("Poisson Distribution")
plt.show()

# Application in Machine learning
# Gaussian Distribution 
# - used in gaussian naive baues and kernal density estimation 
# Bernoulli Distribution 
# - MOdels binary classification problems
# Binomial Distribution 
# - used in logistic regression to model binary outcomes 
# Poisson Distribution 
# models and count data 



 