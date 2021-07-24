
import pandas
import numpy 
import matplotlib.pyplot as paint
import xlrd


data = pandas.read_excel('C:\\Users\\Nast\\source\\repos\\Test11\\test.xlsx') 
print(data.head())

X=data.iloc[:,1:].values
X=(X-X.mean(axis=0))/X.std(axis=0)

from scipy.cluster.hierarchy import linkage,fcluster,dendrogram

Z=linkage(X,method='average',metric='euclidean') 

dendogr=dendrogram(Z)