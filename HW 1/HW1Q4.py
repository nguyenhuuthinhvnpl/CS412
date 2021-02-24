import numpy
from scipy import stats


table_q4 = numpy.array([[150,40],[15,3300]])
# Part A
sum = numpy.sum(table_q4)
beer = table_q4[0][1]
diaper = table_q4 [1][0]
dis = (beer + diaper)/sum;

# Part B
set1 = table_q4[0][0]
set2 = table_q4[0][1]
set3 = table_q4[1][0]
jac = set1 / (set1+set2+set3)
# Part C
chi =  stats.chi2_contingency(table_q4)[0]
# Part D
chi_2 =  stats.chi2_contingency(table_q4)[1]
freedom = stats.chi2_contingency(table_q4)[2]

print()
print("a) Calculate the distance between the binary attributes Buy Beer and Buy Diaper")
print("by assuming they are symmetric binary variables.")
print("=========================================================================================")
print("Distance: ", dis)
print()


print()
print("b) Calculate the distance between the binary attributes Buy Beer and Buy Diaper")
print("by assuming they are symmetric binary variables.")
print("=========================================================================================")
print("Jaccard Coefficient : ", jac)
print()

print()
print("c) Compute the χ2 statistic for the contingency table.")
print("=========================================================================================")
print("χ2: ", chi)
print()

print()
print("d) Consider a hypothesis test based on the χ2 statistic where the null hypothesis")
print("is that Buy Beer and Buy Diaper are independent. Can you reject the null hypothesis")
print("at a significance level of α = 0.05? Explain your answer, and also mention the degrees")
print("of freedom used for the hypothesis test.")
print("=========================================================================================")
print("If the value was more than 0.05 we could not reject the null hypothesis")
print("The value based on info given was: ", chi_2)
if(chi_2<0.05):
	print("We were able to reject")
	print("P value: ", chi_2)
	print("Deg of freedom: ", freedom)
else:
	print("We were not able to reject")
print()

