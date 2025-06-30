# # Measure of central tendency and Dispersion 
# # Central Tendency
# # - Mean = the avarage of a dataset
# # - Median = The middle value when data is shorted 
# # - Mode = the most frequently occuring value 

# from statistics import mode


# data = [10,20,30,40,50]
# mean = sum(data) / len(data)
# print("Mean: ",mean)

# sorted_data = sorted(data)
# median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else\
#     (sorted_data[len(data) //2 -1] + sorted_data[len(data)//2]) /2
    
# print ("median", median)

# print ("Mode: ", mode(data))

# # Dispersion
# # Variance : the average squared deviation from the mean 

# variance = sum ((x - mean) ** 2 for x in data ) / len(data)
# print("Variance :", variance)

# std_var = variance**0.5
# print("Standard Deviation: ", std_var)

# # Hypothesis Testing 
# # What is Hypothesis Testing
# # -> Hypothesis testing is a statistical method used to determine if there is
# # enough evidence in a sample data to draw conclusions about a population parameter

# # Steps :
# #       - Formulate Hypotheses
# #           - NUll Hypothesis 
# #           - Alternative Hypothesis
# #       - calculate test statistic
# #       - Determine P-value
# #       - Interpret Results

# # Confidence Intervals and statistical significance
# # - Confidence Interval 
# #       - Range of values within which the true population parameter is expected to lie 
# #       - Formula: x̄ ± z*(σ/√n) 
#         # Where:
#         # x̄ is the sample mean. 
#         # z is the z-score corresponding to the desired confidence level (e.g., 1.96 for 95%, 2.576 for 99%). 
#         # σ is the population standard deviation. 
#         # n is the sample size. 

import scipy.stats as stats

data = [10,20,30,40,50]
mean = sum(data) / len(data)
variance = sum ((x - mean) ** 2 for x in data ) / len(data)

std_var = variance**0.5

sample_mean = mean
z_score = 1.96
ci =(sample_mean - z_score * (std_var / len(data)**0.5),
     sample_mean + z_score * (std_var) / len(data) **0.5 )

print("95% confidence level at ", ci)









