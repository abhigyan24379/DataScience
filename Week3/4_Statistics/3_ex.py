from scipy.stats import ttest_ind

#sample Dataset 
group1 = [2.1,2.5,2.8,3.0,3.2]
group2 = [1.8,2.0,2.4,2.7,2.9]

#perform t-test
t_stats, p_value = ttest_ind(group1,group2)
print("T-statistic: ", t_stats)
print("P_value:", p_value)

#interpretation 
alpha = 0.05
if p_value < alpha:
    print("reject the null hypothesis: significant difference\n")
else:
    print("failed to reject the null hypothesis difference ")

