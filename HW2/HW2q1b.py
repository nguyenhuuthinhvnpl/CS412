import numpy
from matplotlib import pyplot as plt  

data_1 = numpy.array([13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45,
46, 52, 70])
data_2 = numpy.array([5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215])

# this is for part b 
plt.hist(data_1, bins = [10, 20, 30, 40, 50, 60, 70])
plt.title("Histogram for Data 1")  
plt.show() 

plt.hist(data_2)
plt.title("Histogram for Data 2")  
plt.show() 


data_1b_bin_1 = numpy.array([13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30])
data_1b_bin_2 = numpy.array([33, 33, 35, 35, 35, 35, 36, 40, 45, 46])
data_1b_bin_3 = numpy.array([52, 70])


data_2b_bin_1 = numpy.array([5, 10, 11, 13, 15, 35, 50, 55, 72])
data_2b_bin_2 = numpy.array([92])
data_2b_bin_3 = numpy.array([204, 215])


# Splitting into bins here
data_1_bins = numpy.array_split (data_1, 3)
data_2_bins = numpy.array_split (data_2, 3)

# hard coding each bin for ds1
data_1_bin_1 = data_1_bins[0]
data_1_bin_2 = data_1_bins[1]
data_1_bin_3 = data_1_bins[2]

# hard coding each bin for ds2
data_2_bin_1 = data_2_bins[0]
data_2_bin_2 = data_2_bins[1]
data_2_bin_3 = data_2_bins[2]




print("\n Splitting into bins")
print("\n Data Set 1 for EQUAL FREQ")
print ("Bin 1: ", data_1_bin_1)
print ("Bin 2: ", data_1_bin_2)
print ("Bin 3: ", data_1_bin_3)

print("\n Data Set 2 for EQUAL FREQ")
print ("Bin 1: ", data_2_bin_1)
print ("Bin 2: ", data_2_bin_2)
print ("Bin 3: ", data_2_bin_3)

print("\n Data Set 1 for EQUAL WIDTH")
print ("Bin 1: ", data_1b_bin_1)
print ("Bin 2: ", data_1b_bin_2)
print ("Bin 3: ", data_1b_bin_3)

print("\n Data Set 2 for EQUAL WIDTH")
print ("Bin 1: ", data_2b_bin_1)
print ("Bin 2: ", data_2b_bin_2)
print ("Bin 3: ", data_2b_bin_3)

# ds1 eqf (equal freq)
ds1b_var_bin_1_eqf = numpy.var(data_1_bin_1, dtype = numpy.float32)
ds1b_var_bin_2_eqf = numpy.var(data_1_bin_2, dtype = numpy.float32)
ds1b_var_bin_3_eqf = numpy.var(data_1_bin_3, dtype = numpy.float32)

# ds2 eqf (equal freq)
ds2b_var_bin_1_eqf = numpy.var(data_2_bin_1, dtype = numpy.float32)
ds2b_var_bin_2_eqf = numpy.var(data_2_bin_2, dtype = numpy.float32)
ds2b_var_bin_3_eqf = numpy.var(data_2_bin_3, dtype = numpy.float32)

# ds1 eqw (equal width)
ds1b_var_bin_1_eqw = numpy.var(data_1b_bin_1, dtype = numpy.float32)
ds1b_var_bin_2_eqw = numpy.var(data_1b_bin_2, dtype = numpy.float32)
ds1b_var_bin_3_eqw = numpy.var(data_1b_bin_3, dtype = numpy.float32)

# ds2 eqw (equal width)
ds2b_var_bin_1_eqw = numpy.var(data_2b_bin_1, dtype = numpy.float32)
ds2b_var_bin_2_eqw = numpy.var(data_2b_bin_2, dtype = numpy.float32)
ds2b_var_bin_3_eqw = numpy.var(data_2b_bin_3, dtype = numpy.float32)

ds1_var_og = numpy.var(data_1, dtype = numpy.float32)
ds2_var_og = numpy.var(data_2, dtype = numpy.float32)

print ("\n Variances of Original Data")
print ("Variance Original Data 1: ", ds1_var_og)
print ("Variance Original Data 2: ", ds2_var_og)
print ("\n")
print ("\n Variances of Each Bin for Equal Freq")
print ("Variance Equal-Freq Data 1, Bin 1: ", ds1b_var_bin_1_eqf)
print ("Variance Equal-Freq Data 1, Bin 2: ", ds1b_var_bin_2_eqf)
print ("Variance Equal-Freq Data 1, Bin 3: ", ds1b_var_bin_3_eqf)
ds1eqf_mean = (ds1b_var_bin_1_eqf + ds1b_var_bin_2_eqf + ds1b_var_bin_3_eqf) / 3
print ("Average Variance for Equal-Freq Data 1: ", ds1eqf_mean)
print ("\n")
print ("Variance Equal-Freq Data 2, Bin 1: ", ds2b_var_bin_1_eqf)
print ("Variance Equal-Freq Data 2, Bin 2: ", ds2b_var_bin_2_eqf)
print ("Variance Equal-Freq Data 2, Bin 3: ", ds2b_var_bin_3_eqf)
ds2eqf_mean = (ds2b_var_bin_1_eqf + ds2b_var_bin_2_eqf + ds2b_var_bin_3_eqf) / 3
print ("Average Variance for Equal-Freq Data 2: ", ds2eqf_mean)
print ("\n")
print ("\n Variances of Each Bin for Equal Width")
print ("Variance Equal-Width Data 1, Bin 1: ", ds1b_var_bin_1_eqw)
print ("Variance Equal-Width Data 1, Bin 2: ", ds1b_var_bin_2_eqw)
print ("Variance Equal-Width Data 1, Bin 3: ", ds1b_var_bin_3_eqw)
ds1eqw_mean = (ds1b_var_bin_1_eqw + ds1b_var_bin_2_eqw + ds1b_var_bin_3_eqw) / 3
print ("Average Variance for Equal-Freq Data 2: ", ds1eqw_mean)
print ("\n")
print ("Variance Equal-Width Data 2, Bin 1: ", ds2b_var_bin_1_eqw)
print ("Variance Equal-Width Data 2, Bin 2: ", ds2b_var_bin_2_eqw)
print ("Variance Equal-Width Data 2, Bin 3: ", ds2b_var_bin_3_eqw)
ds2eqw_mean = (ds2b_var_bin_1_eqw + ds2b_var_bin_2_eqw + ds2b_var_bin_3_eqw) / 3
print ("Average Variance for Equal-Freq Data 2: ", ds2eqw_mean)

