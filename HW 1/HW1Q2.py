import numpy
import pandas
from scipy import stats

# Reading Data
data_table = pandas.read_table('data.online.scores.txt', names = ['ID#', 'Mid-Term', 'Final'])
finals = data_table['Final']
mid = data_table['Mid-Term']
# https://numpy.org/doc/stable/reference/generated/numpy.array.html
mid_term_score_arr = numpy.array(mid)
final_score_arr = numpy.array(finals)

var_final = numpy.var(final_score_arr, dtype = numpy.float32)
var_mid = numpy.var(mid_term_score_arr, dtype = numpy.float32)

mid_norm = stats.zscore(mid_term_score_arr)
final_norm = stats.zscore(final_score_arr)
var_mid_norm = numpy.var(mid_norm, dtype = numpy.float32)
var_final_norm = numpy.var(final_norm, dtype = numpy.float32)

given_score = 90
mid_std = numpy.std(mid_term_score_arr)
mid_mean = numpy.mean(mid_term_score_arr)
b_norm = (given_score - mid_mean) / mid_std

corr_o_mid_o_fin = stats.pearsonr(mid_term_score_arr, final_score_arr)

stack = numpy.stack((mid_term_score_arr, final_score_arr), axis = 0)
my_cov = numpy.cov(stack)

print()
print("A) Compute and compare the variance of midterm-original and" 
"midterm-normalized, i.e., the midterm scores before and after normalization.")
print("=====================================================================")
print("Variance MidTerml: ", var_mid)
print("Normalized Variance: ", var_mid_norm)
print()

print()
print("B) Given an original midterm score of 90, what is the corresponding"
	"score after normalization?")
print("=====================================================================")
print("Mean: ", mid_mean)
print("Std-Dev: ", mid_std)
print("Using v' = v - Avg / std-dev")
print("Our score of 90 is normalized to ", b_norm)
print()

print()
print("C) Compute the Pearson’s correlation coefficient between midterm-original"
"and finals-original.?")
print("=====================================================================")
print("Pearson’s correlation coefficient: ", corr_o_mid_o_fin)
print()

print()
print("D) Compute the Pearson’s correlation coefficient between midterm-normalized"
"and finals-original.")
print("=====================================================================")
# https://www.kite.com/python/answers/how-to-normalize-an-array-in-numpy-in-python#:~:text=Use%20numpy.,()%20to%20normalize%20an%20array&text=Call%20numpy.-,linalg.,norm%20to%20normalize%20the%20array.&text=Further%20Reading%20Normalizing%20a%20dataset,to%20%5B0%2C%201%5D%20.
print("Pearson’s correlation coefficient: ", corr_o_mid_o_fin)
print()

print()
print("E) Compute the covariance between midterm-original and finals-original.")
print("=====================================================================")
print("Covariance: ", my_cov)
print()

