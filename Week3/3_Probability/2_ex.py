# Problem 
# - A disease affects 1% of the population 
# - A test is 95% accurate for disease individuals and 90% accurate for non diseased individual 
# - Find the probability of having the disease given a positive test result 

def bayes_theorem ( prior, sensitivity , specificity ):
    # truly positive = ( sensitivity * prior ) ,, Falsely positive = (1-specificity) * (1 - prior)
    evidence = ( sensitivity * prior ) + ((1-specificity) * (1 - prior))
    
    posterior = ( sensitivity * prior ) /evidence
    return posterior

prior = 0.01
sensitivity  = 0.95
specificity = 0.90

posterior = bayes_theorem(prior, sensitivity, specificity)
print(posterior)


