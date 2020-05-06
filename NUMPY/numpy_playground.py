##
print('not again')
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
c = a + b
c
print(a)

np.where(a<2, a, 999)
a+1
##

e = np.ones((3, 3))

e+1**1

x=np.array([1,2,3])
##
y=x.reshape((3,1))

##
print(x)
print(y)
##
print(x+y)

##
print('aaa')
print('ddd')


# 49. How to compute the row wise counts of all possible values in an array?

np.random.seed(100)
arr = np.random.randint(1,11,size=(6, 10))
arr




# How to drop all missing values from a numpy array?


a=np.array([1,2,3,np.nan,5,6,7,np.nan])
a

np.isna(a)
np.isnan(a)

# Array Creation
np.random.randint(1,100, size=(5,5))
np.arange(10)
np.linspace(1,100,10)
np.indices((2 ,3))
a=np.random.uniform(0,1,1200)


##
def draw_hist(arr, fileName):
    import matplotlib
    matplotlib.use('PS')
    import matplotlib.pyplot as plt
    fig=plt.figure(figsize=(6,6))
    ax=fig.add_subplot(1,1,1)
    ax.hist(a)
    plt.savefig('{}.png'.format(fileName))
##

# Subsetting
a=np.arange(10)
a
a[1:8:2]

a[1:8]
a[5:]
a.shape



x = np.array([[1, 2], [3, 4], [5, 6]])
x
x[[0, 1, 2], [0, 1, 0]]
import sys
import numpy as np
import random
np.empty([5,5],dtype='U10')
np.zeros([5,5],dtype='I')

print (np.__version__)

ar=np.arange(12)
ar[5:]
ar[:4]
ar[2:8:2]
ar[:-1]
ar[-1:-8:-2]
ar[:]
# ads fs
ar2=np.random.random_integers(12,size=12).reshape([3,4])
ar2
ar2=np.random.random_integers(1,12)
ar2
np.random.randint(1,12+1)
np.random.random_integers(1, 6, 1000)

np.random.randint(2,9+1, size=(2,4))
np.random.randint(2,8+1, size=(2,4))

np.random.randint(2,9+1,size=(2,4))

np.random.randint(5,size=(2,4))

np.random.randint(1,5,10,int)

a=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
a
a=np.linspace(1,10,endpoint=True)
a


np.array([[1, 2], [3, 4]])==np.array([(1, 2), (3, 4)])

a={1,2,3,4}
b={4,5,6,7}
c=a.union(b)
c

vector = np.array([10,20,30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])


world_alcohol = np.genfromtxt("/home/paperspace/data/kaggle/other_csv/world_alcohol.csv", delimiter=",")
world_alcohol
world_alcohol_dtype=type(world_alcohol)

print (world_alcohol)
numbers = array([1, 2, 3, 4])
a= np.array([[ 1., 0., 0.],[ 0., 1., 2.]])
b = arange(15).reshape(3, 5)
b
b.dtype.name

a.size
b.ndim

##
import numpy as np
y = np.eye(3)
y
z = np.arange(1,10).reshape(3,3)
z
t = np.dot(y,z)
t
y
z
print(t)
##
np.dot (np.array(10))


np.arange(10)

np.array([1,10])


a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]


a=[1,2]
b=[2,3]


np.dot(a, b)
