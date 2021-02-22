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


# Part A
# Mid-Term Data
min_mid = numpy.min(mid_term_score_arr)
max_mid = numpy.max(mid_term_score_arr)
#Final Data
min_val_final = numpy.min(final_score_arr)
max_val_final = numpy.max(final_score_arr)


# Part B
# https://numpy.org/doc/stable/reference/generated/numpy.around.html
#numpy.median(final_score_arr)
mq1 = numpy.percentile(mid_term_score_arr,25) # Q1
mq2 = numpy.percentile(mid_term_score_arr,50) # median
mq3 = numpy.percentile(mid_term_score_arr,75) # Q3
q1 = numpy.percentile(final_score_arr,25) # Q1
q2 = numpy.percentile(final_score_arr,50) # median
q3 = numpy.percentile(final_score_arr,75) # Q3

# Part C
finals_mean = numpy.mean(final_score_arr)
# https://numpy.org/doc/stable/reference/generated/numpy.around.html
finals_mean_rounded = numpy.around(finals_mean, decimals = 3)
mid_mean = numpy.mean(mid_term_score_arr)
mid_mean_rounded = numpy.around(mid_mean, decimals =3)

# Part D
# https://stackoverflow.com/questions/16330831/most-efficient-way-to-find-mode-in-numpy-array
mid_term_mode = mid.mode()
final_mode = finals.mode()

# Part E
# https://www.geeksforgeeks.org/numpy-var-in-python/
mid_var = numpy.var(mid_term_score_arr, dtype = numpy.float32)
var_final = numpy.var(final_score_arr, dtype = numpy.float32)

print()
print()
print("A) Maximum and minimum.")
print("========================================================")
print("Mid-Term", min_mid, ',' , max_mid)
print("Final: ", min_val_final, ',', max_val_final)
print()
print("B) First quartile Q1, median, and third quartile Q3")
print("========================================================")
print("Mid-Term:",mq1,',',mq2,',',mq3)
print("Final: ",q1,',',q2,',',q3)
print()
print("C) Mean")
print("========================================================")
print("Mid-Term: ", mid_mean_rounded)
print("Final: ", finals_mean_rounded)
print()
print("D) Mode")
print("========================================================")
print("Mid-Term: ", *mid_term_mode)
print("Final: ", *final_mode)
print()
print("E) Variance")
print("========================================================")
print("Mid-Term: ", mid_var)
print("Final: " , var_final)
print()
print()

