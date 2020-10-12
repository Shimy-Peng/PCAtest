import requests

#load iris from web
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

try:
    htmlfile = requests.get(url)
    print('download success!')
except Exception as err:
    print('download fail')

file = 'iris.csv'
with open(file, 'wb') as fileobj:
    for diskstorage in htmlfile.iter_content(10240):
        size = fileobj.write(diskstorage) 

#plot
import pandas as pd
import matplotlib.pyplot as plt
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(file , names = colName)

iris_setosa = iris[iris['species'] == 'Iris-setosa']
iris_versicolor = iris[iris['species'] == 'Iris-versicolor']
iris_virginica = iris[iris['species'] == 'Iris-virginica']

#plt.subplot(121)
plt.plot(iris_setosa['petal_len'],iris_setosa['petal_wd'],
         '*',color='g',label='setosa')
plt.plot(iris_versicolor['petal_len'],iris_versicolor['petal_wd'],
         'x',color='b',label='versicolor')
plt.plot(iris_virginica['petal_len'],iris_virginica['petal_wd'],
         '.',color='r',label='virginica')
plt.xlabel('petal Length')
plt.ylabel('petal Width')
plt.title('Iris dataset')
plt.legend()


plt.show()