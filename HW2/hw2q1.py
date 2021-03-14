import numpy
data_1 = numpy.array([13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45,
46, 52, 70])
data_2 = numpy.array([5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215])
# calc # of bins
num_bin_ds1 = len(data_1) / 3
num_bin_ds2 = len(data_2) / 3
print ("Num bins needed for data set 1: ", num_bin_ds1)
print ("Num bins needed for data set 2: ", num_bin_ds2)

# Splitting into bins here
data_1_bins = numpy.array_split (data_1, num_bin_ds1)
data_2_bins = numpy.array_split (data_2, num_bin_ds2)

# hard coding each bin for ds1
data_1_bin_1 = data_1_bins[0]
data_1_bin_2 = data_1_bins[1]
data_1_bin_3 = data_1_bins[2]
data_1_bin_4 = data_1_bins[3]
data_1_bin_5 = data_1_bins[4]
data_1_bin_6 = data_1_bins[5]
data_1_bin_7 = data_1_bins[6]
data_1_bin_8 = data_1_bins[7]
data_1_bin_9 = data_1_bins[8]

# hard coding each bin for ds2
data_2_bin_1 = data_2_bins[0]
data_2_bin_2 = data_2_bins[1]
data_2_bin_3 = data_2_bins[2]
data_2_bin_4 = data_2_bins[3]

# finding means 
# ds1
data_1_bin_1_mean = numpy.mean(data_1_bins[0])
data_1_bin_2_mean = numpy.mean(data_1_bins[1])
data_1_bin_3_mean = numpy.mean(data_1_bins[2])
data_1_bin_4_mean = numpy.mean(data_1_bins[3])
data_1_bin_5_mean = numpy.mean(data_1_bins[4])
data_1_bin_6_mean = numpy.mean(data_1_bins[5])
data_1_bin_7_mean = numpy.mean(data_1_bins[6])
data_1_bin_8_mean = numpy.mean(data_1_bins[7])
data_1_bin_9_mean = numpy.mean(data_1_bins[8])

# ds2
data_2_bin_1_mean = numpy.mean(data_2_bins[0])
data_2_bin_2_mean = numpy.mean(data_2_bins[1])
data_2_bin_3_mean = numpy.mean(data_2_bins[2])
data_2_bin_4_mean = numpy.mean(data_2_bins[3])

print("\n Splitting into bins")
print("\n Data Set 1")
print (data_1)
print ("Bin 1: ", data_1_bin_1)
print ("Bin 2: ", data_1_bin_2)
print ("Bin 3: ", data_1_bin_3)
print ("Bin 4: ", data_1_bin_4)
print ("Bin 5: ", data_1_bin_5)
print ("Bin 6: ", data_1_bin_6)
print ("Bin 7: ", data_1_bin_7)
print ("Bin 8: ", data_1_bin_8)
print ("Bin 9: ", data_1_bin_9)


print("\n Data Set 2")
print (data_2)
print ("Bin 1: ", data_2_bin_1)
print ("Bin 2: ", data_2_bin_2)
print ("Bin 3: ", data_2_bin_3)
print ("Bin 4: ", data_2_bin_4)


print("\n We now find the mean of each bin")
print("\n Mean of each bin for data set 1")
print ("Bin 1: ", data_1_bin_1_mean)
print ("Bin 2: ", data_1_bin_2_mean)
print ("Bin 3: ", data_1_bin_3_mean)
print ("Bin 4: ", data_1_bin_4_mean)
print ("Bin 5: ", data_1_bin_5_mean)
print ("Bin 6: ", data_1_bin_6_mean)
print ("Bin 7: ", data_1_bin_7_mean)
print ("Bin 8: ", data_1_bin_8_mean)
print ("Bin 9: ", data_1_bin_9_mean)

print("\n Mean of each bin for data set 2")
print ("Bin 1: ", data_2_bin_1_mean)
print ("Bin 2: ", data_2_bin_2_mean)
print ("Bin 3: ", data_2_bin_3_mean)
print ("Bin 4: ", data_2_bin_4_mean)

data_1_bin_1 = numpy.array(data_1_bin_1.astype('float64'))
data_1_bin_2 = numpy.array(data_1_bin_2.astype('float64'))
data_1_bin_3 = numpy.array(data_1_bin_3.astype('float64'))
data_1_bin_4 = numpy.array(data_1_bin_4.astype('float64'))
data_1_bin_5 = numpy.array(data_1_bin_5.astype('float64'))
data_1_bin_6 = numpy.array(data_1_bin_6.astype('float64'))
data_1_bin_7 = numpy.array(data_1_bin_7.astype('float64'))
data_1_bin_8 = numpy.array(data_1_bin_8.astype('float64'))
data_1_bin_9 = numpy.array(data_1_bin_9.astype('float64'))

data_2_bin_1 = numpy.array(data_2_bin_1.astype('float64'))
data_2_bin_2 = numpy.array(data_2_bin_2.astype('float64'))
data_2_bin_3 = numpy.array(data_2_bin_3.astype('float64'))
data_2_bin_4 = numpy.array(data_2_bin_4.astype('float64'))

length_ds1 = len(data_1_bin_1)
for x in range(length_ds1):
    data_1_bin_1[x] = round(data_1_bin_1_mean,2)
for x in range(length_ds1):
    data_1_bin_2[x] = round(data_1_bin_2_mean,2)
for x in range(length_ds1):
    data_1_bin_3[x] = round(data_1_bin_3_mean, 2)
for x in range(length_ds1):
    data_1_bin_4[x] = round(data_1_bin_4_mean, 2)
for x in range(length_ds1):
    data_1_bin_5[x] = round(data_1_bin_5_mean, 2)
for x in range(length_ds1):
    data_1_bin_6[x] = round(data_1_bin_6_mean, 2)
for x in range(length_ds1):
    data_1_bin_7[x] = round(data_1_bin_7_mean, 2)
for x in range(length_ds1):
    data_1_bin_8[x] = round(data_1_bin_8_mean, 2)
for x in range(length_ds1):
    data_1_bin_9[x] = round(data_1_bin_9_mean, 2)

length_ds2 = len(data_2_bin_1)
for x in range(length_ds2):
    data_2_bin_1[x] = round(data_2_bin_1_mean,2)
for x in range(length_ds2):
    data_2_bin_2[x] = round(data_2_bin_2_mean,2)
for x in range(length_ds2):
    data_2_bin_3[x] = round(data_2_bin_3_mean,2)
for x in range(length_ds2):
    data_2_bin_4[x] = round(data_2_bin_4_mean,2)

print("Replace all values with each bins mean")
print("\n Data Set 1")
print ("Bin 1: ", data_1_bin_1)
print ("Bin 2: ", data_1_bin_2)
print ("Bin 3: ", data_1_bin_3)
print ("Bin 4: ", data_1_bin_4)
print ("Bin 5: ", data_1_bin_5)
print ("Bin 6: ", data_1_bin_6)
print ("Bin 7: ", data_1_bin_7)
print ("Bin 8: ", data_1_bin_8)
print ("Bin 9: ", data_1_bin_9)

print("\n Data Set 2")
print ("Bin 1: ", data_2_bin_1)
print ("Bin 2: ", data_2_bin_2)
print ("Bin 3: ", data_2_bin_3)
print ("Bin 4: ", data_2_bin_4)

ds1 = numpy.concatenate((data_1_bin_1, data_1_bin_2, data_1_bin_3, data_1_bin_4, data_1_bin_5, data_1_bin_6, data_1_bin_7, data_1_bin_8, data_1_bin_9))
ds2 = numpy.concatenate((data_2_bin_1, data_2_bin_2, data_2_bin_3, data_2_bin_4))
print ("New Data Sets")
print ("Data Set 1: ",ds1)
print ("Data Set 2: ",ds2)

ds1_var_bin = numpy.var(ds1, dtype = numpy.float32)
ds2_var_bin = numpy.var(ds2, dtype = numpy.float32)
ds1_var_og = numpy.var(data_1, dtype = numpy.float32)
ds2_var_og = numpy.var(data_2, dtype = numpy.float32)
print ("Variances")
print ("Variance Original Data 1: ", ds1_var_og)
print ("Variance Original Data 2: ", ds2_var_og)
print ("Variance New Data 1: ", ds1_var_bin)
print ("Variance New Data 2: ", ds2_var_bin)

ds1_mean_og = numpy.mean(data_1)
ds2_mean_og = numpy.mean(data_2)
ds1_mean_new = numpy.mean(ds1)
ds2_mean_new = numpy.mean(ds2)
print("\n Means")
print("DS1 Mean OG: ", ds1_mean_og)
print("DS2 Mean OG: ", ds2_mean_og)
print("DS1 Mean New: ", ds1_mean_new)
print("DS2 Mean New: ", ds2_mean_new)