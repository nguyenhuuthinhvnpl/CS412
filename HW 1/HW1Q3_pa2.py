import numpy
import pandas
from scipy import stats
from scipy.spatial import distance
from scipy.stats import entropy

# Reading Data
# I was changing text file before, I do not think I should do that
data_table = "data.libraries.inventories.txt"
parse_data = pandas.read_csv(data_table, "\t")
cml = numpy.array(parse_data.loc[parse_data['library'] == 'CML'])[0]
cbl = numpy.array(parse_data.loc[parse_data['library'] == 'CBL'])[0]
#get rid of the book stuff
cml = numpy.delete(cml, 0)
cbl = numpy.delete(cbl, 0)
#Part A
q3p1 = distance.minkowski(cml, cbl, 1)
q3p2 = distance.minkowski(cml, cbl, 2)
q3p3 = distance.minkowski(cml, cbl, float('inf'))

#Part B
q3p4 = 1 - distance.cosine(list(cml), list(cbl))

#Part C
kl1 = entropy(list(cml), list(cbl))
kl2 = entropy(list(cbl), list(cml))
kl1perc = kl1 * 100
kl2perc = kl2 * 100


print()
print("a) Each library has multiple copies of each book. Based on all the books (treat")
print("the counts of the 100 books as a feature vector for each of the libraries), compute the")
print("Minkowski distance of the vectors for CML and CBL with regard to different h values:")
print("=========================================================================================")
print("i) ","	",q3p1)
print("ii) ","	",q3p2)
print("iii) ","	",q3p3)
print()


print()
print("b) Compute the cosine similarity between the feature vectors for CML and CBL.")
print("=========================================================================================")
print("Cosine similarity: ", q3p4)
print()

print()
print("c) Compute the Kullback-Leibler (KL) divergence between CML and CBL")
print("=========================================================================================")
print("KL(CML || CBL): ", kl1, "in '%' it will be ", round(kl1perc,4),"%")
print("KL(CBL || CML: ", kl2, "in '%' it will be ", round(kl2perc,2),"%")
print()

