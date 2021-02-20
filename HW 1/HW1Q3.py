import numpy
import pandas
from scipy import stats
from scipy.spatial import distance

# Reading Data
data_table = pandas.read_table('data.libraries.inventories.txt', names = ['library', 'CML', 'CBL'])
cml = data_table['CML']
cbl = data_table['CBL']


q3p1 = distance.minkowski(cml, cbl, 1)
q3p2 = distance.minkowski(cml, cbl, 2)
q3p3 = distance.minkowski(cml, cbl, float('inf'))

q3p4 = 1 - distance.cosine(cml, cbl)

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
