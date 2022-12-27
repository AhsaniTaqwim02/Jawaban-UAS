import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

#Database: Gerbang LOgika AND
#Membaca data dari file
FileDB = 'Data Base.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)

#x = Data, y=Target
X = Database[[u'a', u'b']]
y = Database.Target


clf = svm.SVC()
clf.fit(X.values,y)

print(clf.predict( [[2,4]] ))
print(clf.predict( [[3,5]] ))
print(clf.predict( [[4,6]] ))
print(clf.predict( [[5,7]] ))
print(clf.predict( [[6,8]] ))
print(clf.predict( [[7,9]] ))
print(clf.predict( [[8,10]] ))
print(clf.predict( [[9,11]] ))
print(clf.predict( [[10,12]] ))
print(clf.predict( [[11,13]] ))
