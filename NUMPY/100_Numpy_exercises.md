#### 3. Create a null vector of size 10 (★☆☆)

```python
Z = np.zeros(10)
print(Z)
```

    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]


#### 4.  How to find the memory size of any array (★☆☆)


```python
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
```

    800 bytes


#### 5.  How to get the documentation of the numpy add function from the command line? (★☆☆)


```python
# %run `python -c "import numpy; numpy.info(numpy.add)"`
```

#### 6.  Create a null vector of size 10 but the fifth value which is 1 (★☆☆)


```python
Z = np.zeros(10)
Z[4] = 1
print(Z)
```

    [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]


#### 7.  Create a vector with values ranging from 10 to 49 (★☆☆)


```python
Z = np.arange(10,50)
print(Z)
```

    [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
     34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]


#### 8.  Reverse a vector (first element becomes last) (★☆☆)


```python
Z = np.arange(50)
Z = Z[::-1]
print(Z)
```

    [49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26
     25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2
      1  0]


#### 9.  Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)


```python
Z = np.arange(9).reshape(3,3)
print(Z)
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]


#### 10. Find indices of non-zero elements from \[1,2,0,0,4,0\] (★☆☆)


```python
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
```

    (array([0, 1, 4]),)


#### 11. Create a 3x3 identity matrix (★☆☆)


```python
Z = np.eye(3)
print(Z)
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]


#### 12. Create a 3x3x3 array with random values (★☆☆)


```python
Z = np.random.random((3,3,3))
print(Z)
```

    [[[0.47063423 0.01733729 0.55663328]
      [0.28091698 0.18678069 0.73694498]
      [0.40896131 0.08431603 0.89088847]]
    
     [[0.28889231 0.52634132 0.52397885]
      [0.21273592 0.12012295 0.80346119]
      [0.24895858 0.00617297 0.15295567]]
    
     [[0.50392437 0.50943268 0.65126251]
      [0.52826781 0.68227997 0.58648481]
      [0.42401926 0.6941513  0.58653929]]]


#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)


```python
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
```

    0.00730426757203162 0.9985989422488284


#### 14. Create a random vector of size 30 and find the mean value (★☆☆)


```python
Z = np.random.random(30)
m = Z.mean()
print(m)
```

    0.4714248780466014


#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)


```python
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
```

    [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]


#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)


```python
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
```

    [[0. 0. 0. 0. 0. 0. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 0. 0. 0. 0. 0. 0.]]


#### 17. What is the result of the following expression? (★☆☆)


```python
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
```

    nan
    False
    False
    nan
    False


#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)


```python
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
```

    [[0 0 0 0 0]
     [1 0 0 0 0]
     [0 2 0 0 0]
     [0 0 3 0 0]
     [0 0 0 4 0]]


#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)


```python
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
```

    [[0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]]


#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?


```python
print(np.unravel_index(100,(6,7,8)))
```

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)


```python
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
```

#### 22. Normalize a 5x5 random matrix (★☆☆)


```python
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
```

#### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)


```python
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
```

#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)

[numpy中矩阵乘法，星乘(*)和点乘(.dot)的区别](https://blog.csdn.net/like4501/article/details/79753346)


```python
a=np.ones((5,3))
a
```




    array([[1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.]])




```python
b=np.ones((3,2))
b
```




    array([[1., 1.],
           [1., 1.],
           [1., 1.]])




```python
np.dot(a,b)
```




    array([[3., 3.],
           [3., 3.],
           [3., 3.],
           [3., 3.],
           [3., 3.]])




```python
# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)
```

    [[3. 3.]
     [3. 3.]
     [3. 3.]
     [3. 3.]
     [3. 3.]]


#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)


```python
# Author: Evgeni Burovski

Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)
```

    [ 0  1  2  3 -4 -5 -6 -7 -8  9 10]


#### 26. What is the output of the following script? (★☆☆)


```python
# Author: Jake VanderPlas

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
```

#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)


```python
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
```

#### 28. What are the result of the following expressions?


```python
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))
```

#### 29. How to round away from zero a float array ? (★☆☆)


```python
# Author: Charles R Harris

Z = np.random.uniform(-10,+10,10)
Z
```




    array([ 4.80204573, -4.82257175,  2.26487914,  8.27706642,  8.37127879,
            8.08281622,  5.27933741,  6.02341749, -2.25401614,  4.25563497])




```python
print (np.copysign((np.abs(Z)), Z))
```

    [ 5. -5.  3.  9.  9.  9.  6.  7. -3.  5.]


#### 30. How to find common values between two arrays? (★☆☆)


```python
Z1 = np.random.randint(0,10,10)
print('Z1:')
print(Z1)
Z2 = np.random.randint(0,10,10)
print('Z2:')
print(Z2)
print('intersect:')
print(np.intersect1d(Z1,Z2))
```

    Z1:
    [0 3 1 1 0 2 8 6 3 5]
    Z2:
    [4 9 0 3 5 0 6 9 5 7]
    intersect:
    [0 3 5 6]


#### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)


```python
# Suicide mode on
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0

# Back to sanity
_ = np.seterr(**defaults)

An equivalent way, with a context manager:

with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0
```

#### 32. Is the following expressions true? (★☆☆)


```python
np.sqrt(-1) == np.emath.sqrt(-1)
```

    /home/paperspace/anaconda3/envs/bioinfo/lib/python3.6/site-packages/ipykernel/__main__.py:1: RuntimeWarning: invalid value encountered in sqrt
      if __name__ == '__main__':





    False



#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)


```python
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
```

#### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)


```python
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)
```

#### 35. How to compute ((A+B)\*(-A/2)) in place (without copy)? (★★☆)


```python
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
```

#### 36. Extract the integer part of a random array using 5 different methods (★★☆)


```python
Z = np.random.uniform(0,10,10)

print (Z - Z%1)
print (np.floor(Z))
print (np.ceil(Z)-1)
print (Z.astype(int))
print (np.trunc(Z))
```

    [5. 3. 3. 6. 2. 8. 4. 0. 5. 4.]
    [5. 3. 3. 6. 2. 8. 4. 0. 5. 4.]
    [5. 3. 3. 6. 2. 8. 4. 0. 5. 4.]
    [5 3 3 6 2 8 4 0 5 4]
    [5. 3. 3. 6. 2. 8. 4. 0. 5. 4.]


#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)


```python
Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)
```

    [[0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]]


#### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)


```python
def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)
```

    [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]


#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)


```python
Z = np.linspace(0,1,11,endpoint=False)[1:]
print(Z)
```

    [0.09090909 0.18181818 0.27272727 0.36363636 0.45454545 0.54545455
     0.63636364 0.72727273 0.81818182 0.90909091]


#### 40. Create a random vector of size 10 and sort it (★★☆)


```python
Z = np.random.random(10)
Z.sort()
print(Z)
```

    [0.11067601 0.2150355  0.22538541 0.31381577 0.34818952 0.434806
     0.74300909 0.82387819 0.82602725 0.94692638]


#### 41. How to sum a small array faster than np.sum? (★★☆)


```python
# Author: Evgeni Burovski

Z = np.arange(10)
np.add.reduce(Z)
```




    45



#### 42. Consider two random array A and B, check if they are equal (★★☆)


```python
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)

# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)
```

    False
    False


#### 43. Make an array immutable (read-only) (★★☆)


```python
Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-56-dcc5e7f145b5> in <module>
          1 Z = np.zeros(10)
          2 Z.flags.writeable = False
    ----> 3 Z[0] = 1
    

    ValueError: assignment destination is read-only


#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)


```python
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)
```

    [0.53038154 0.34669656 1.09519776 0.72102284 0.78209807 0.64494759
     0.51087857 0.70703874 0.14776165 0.90166673]
    [0.08210396 0.58298028 0.46969539 0.11477649 1.17080539 1.1506858
     1.00399813 1.30960336 1.29818542 1.50572799]


#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)


```python
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)
```

    [0.24543365 0.33960135 0.         0.09433534 0.62914061 0.13687389
     0.32926154 0.6281331  0.35675589 0.11756403]


#### 46. Create a structured array with `x` and `y` coordinates covering the \[0,1\]x\[0,1\] area (★★☆)


```python
Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(Z)
```

####  47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))


```python
# Author: Evgeni Burovski

X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C))
```

#### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)


```python
for dtype in [np.int8, np.int32, np.int64]:
   print(np.iinfo(dtype).min)
   print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
   print(np.finfo(dtype).min)
   print(np.finfo(dtype).max)
   print(np.finfo(dtype).eps)
```

#### 49. How to print all the values of an array? (★★☆)


```python
np.set_printoptions(threshold=np.nan)
Z = np.zeros((16,16))
print(Z)
```

    [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]


#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)


```python
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print(Z[index])
```

    97


#### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)


```python
Z = np.zeros(10, [ ('position', [ ('x', float, 1),
                                  ('y', float, 1)]),
                   ('color',    [ ('r', float, 1),
                                  ('g', float, 1),
                                  ('b', float, 1)])])
print(Z)
```

    [((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
     ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
     ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
     ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
     ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))]


#### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)


```python
Z = np.random.random((10,2))
Z
```




    array([[0.61660789, 0.73705913],
           [0.19588693, 0.92491208],
           [0.37493552, 0.37583622],
           [0.23384541, 0.22562328],
           [0.26482967, 0.36498835],
           [0.70443264, 0.01552321],
           [0.38248555, 0.69199332],
           [0.40880089, 0.16311938],
           [0.28724737, 0.71199006],
           [0.36276899, 0.92112663]])




```python
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)
```

    [[0.         0.46075466 0.43461193 0.6388065  0.51203963 0.72686125
      0.23842022 0.61040199 0.3303132  0.31355228]
     [0.46075466 0.         0.57753156 0.70031827 0.56415218 1.04192459
      0.2984463  0.79098702 0.23169487 0.16692499]
     [0.43461193 0.57753156 0.         0.20608335 0.11063894 0.48825589
      0.31624724 0.21539571 0.34740268 0.54542613]
     [0.6388065  0.70031827 0.20608335 0.         0.14276781 0.51535849
      0.48948433 0.18578524 0.48928971 0.70735155]
     [0.51203963 0.56415218 0.11063894 0.14276781 0.         0.56158406
      0.3475272  0.24794917 0.34772509 0.56469629]
     [0.72686125 1.04192459 0.48825589 0.51535849 0.56158406 0.
      0.74917404 0.33042815 0.81185567 0.96791095]
     [0.23842022 0.2984463  0.31624724 0.48948433 0.3475272  0.74917404
      0.         0.52952822 0.09731485 0.22998004]
     [0.61040199 0.79098702 0.21539571 0.18578524 0.24794917 0.33042815
      0.52952822 0.         0.56216927 0.75940366]
     [0.3303132  0.23169487 0.34740268 0.48928971 0.34772509 0.81185567
      0.09731485 0.56216927 0.         0.22235472]
     [0.31355228 0.16692499 0.54542613 0.70735155 0.56469629 0.96791095
      0.22998004 0.75940366 0.22235472 0.        ]]



```python
# Much faster with scipy
import scipy
# Thanks Gavin Heverly-Coulson (#issue 1)
import scipy.spatial

Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)
```

#### 53. How to convert a float (32 bits) array into an integer (32 bits) in place?


```python
Z = np.arange(10, dtype=np.float32)
Z = Z.astype(np.int32, copy=False)
print(Z)
```

#### 54. How to read the following file? (★★☆)


```python
from io import StringIO

# Fake file 
s = StringIO("""1, 2, 3, 4, 5\n
                6,  ,  , 7, 8\n
                 ,  , 9,10,11\n""")
Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
print(Z)
```

#### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)


```python
Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print(index, value)
for index in np.ndindex(Z.shape):
    print(index, Z[index])
```

    (0, 0) 0
    (0, 1) 1
    (0, 2) 2
    (1, 0) 3
    (1, 1) 4
    (1, 2) 5
    (2, 0) 6
    (2, 1) 7
    (2, 2) 8
    (0, 0) 0
    (0, 1) 1
    (0, 2) 2
    (1, 0) 3
    (1, 1) 4
    (1, 2) 5
    (2, 0) 6
    (2, 1) 7
    (2, 2) 8


#### 56. Generate a generic 2D Gaussian-like array (★★☆)


```python
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)
```

#### 57. How to randomly place p elements in a 2D array? (★★☆)


```python
# Author: Divakar

n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(Z)
```

#### 58. Subtract the mean of each row of a matrix (★★☆)


```python
# Author: Warren Weckesser

X = np.random.rand(5, 10)

# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)

# Older versions of numpy
Y = X - X.mean(axis=1).reshape(-1, 1)

print(Y)
```

#### 59. How to sort an array by the nth column? (★★☆)


```python
# Author: Steve Tjoa

Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])
```

#### 60. How to tell if a given 2D array has null columns? (★★☆)


```python
# Author: Warren Weckesser

Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())
```

#### 61. Find the nearest value from a given value in an array (★★☆)


```python
Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)
```

#### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)


```python
A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
it = np.nditer([A,B,None])
for x,y,z in it: z[...] = x + y
print(it.operands[2])
```

#### 63. Create an array class that has a name attribute (★★☆)


```python
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)
```

#### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)


```python
# Author: Brett Olsen

Z = np.ones(10)
Z
```




    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])




```python
I = np.random.randint(0,len(Z),20)
I
```




    array([3, 7, 5, 5, 0, 1, 4, 7, 7, 8, 0, 8, 1, 5, 6, 4, 7, 9, 0, 6])




```python
np.bincount(I, minlength=len(Z))
```




    array([3, 2, 0, 1, 2, 3, 2, 4, 2, 1])




```python
Z += np.bincount(I, minlength=len(Z))
Z
```




    array([10.,  7.,  1.,  4.,  7., 10.,  7., 13.,  7.,  4.])




```python
print(Z)

# Another solution
# Author: Bartosz Telenczuk
np.add.at(Z, I, 1)
print(Z)
```


```python
np.bincount([1,2,3])
```




    array([0, 1, 1, 1])



#### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)


```python
# Author: Alan G Isaac

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print(F)
```

#### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★)


```python
# Author: Nadav Horesh

w,h = 16,16
I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
#Note that we should compute 256*256 first. 
#Otherwise numpy will only promote F.dtype to 'uint16' and overfolw will occur
F = I[...,0]*(256*256) + I[...,1]*256 +I[...,2]
n = len(np.unique(F))
print(n)
```

#### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)


```python
A = np.random.randint(0,10,(3,4,3,4))
# solution by passing a tuple of axes (introduced in numpy 1.7.0)
sum = A.sum(axis=(-2,-1))
print(sum)
# solution by flattening the last two dimensions into one
# (useful for functions that don't accept tuples for axis argument)
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)
```

#### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)


```python
# Author: Jaime Fernández del Río

D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)

# Pandas solution as a reference due to more intuitive code
import pandas as pd
print(pd.Series(D).groupby(S).mean())
```

#### 69. How to get the diagonal of a dot product? (★★★)


```python
# Author: Mathieu Blondel

A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))

# Slow version  
np.diag(np.dot(A, B))

# Fast version
np.sum(A * B.T, axis=1)

# Faster version
np.einsum("ij,ji->i", A, B)
```

#### 70. Consider the vector \[1, 2, 3, 4, 5\], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)


```python
# Author: Warren Weckesser

Z = np.array([1,2,3,4,5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0)
```

#### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)


```python
A = np.ones((5,5,3))
B = 2*np.ones((5,5))
print(A * B[:,:,None])
```

#### 72. How to swap two rows of an array? (★★★)


```python
# Author: Eelco Hoogendoorn

A = np.arange(25).reshape(5,5)
A[[0,1]] = A[[1,0]]
print(A)
```

#### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)


```python
# Author: Nicolas P. Rougier

faces = np.random.randint(0,100,(10,3))
F = np.roll(faces.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = np.sort(F,axis=1)
G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )
G = np.unique(G)
print(G)
```

#### 74. Given an array C that is a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)


```python
# Author: Jaime Fernández del Río

C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print(A)
```

#### 75. How to compute averages using a sliding window over an array? (★★★)


```python
# Author: Jaime Fernández del Río

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
Z = np.arange(20)
print(moving_average(Z, n=3))
```

#### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z\[0\],Z\[1\],Z\[2\]) and each subsequent row is  shifted by 1 (last row should be (Z\[-3\],Z\[-2\],Z\[-1\]) (★★★)


```python
# Author: Joe Kington / Erik Rigtorp
from numpy.lib import stride_tricks

def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.itemsize, a.itemsize)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
Z = rolling(np.arange(10), 3)
print(Z)
```

#### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)


```python
# Author: Nathaniel J. Smith

Z = np.random.randint(0,2,100)
np.logical_not(Z, out=Z)

Z = np.random.uniform(-1.0,1.0,100)
np.negative(Z, out=Z)
```

#### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i  (P0\[i\],P1\[i\])? (★★★)


```python
def distance(P0, P1, p):
    T = P1 - P0
    L = (T**2).sum(axis=1)
    U = -((P0[:,0]-p[...,0])*T[:,0] + (P0[:,1]-p[...,1])*T[:,1]) / L
    U = U.reshape(len(U),1)
    D = P0 + U*T - p
    return np.sqrt((D**2).sum(axis=1))

P0 = np.random.uniform(-10,10,(10,2))
P1 = np.random.uniform(-10,10,(10,2))
p  = np.random.uniform(-10,10,( 1,2))
print(distance(P0, P1, p))
```

#### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P\[j\]) to each line i (P0\[i\],P1\[i\])? (★★★)


```python
# Author: Italmassov Kuanysh

# based on distance function from previous question
P0 = np.random.uniform(-10, 10, (10,2))
P1 = np.random.uniform(-10,10,(10,2))
p = np.random.uniform(-10, 10, (10,2))
print(np.array([distance(P0,P1,p_i) for p_i in p]))
```

#### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)


```python
# Author: Nicolas Rougier

Z = np.random.randint(0,10,(10,10))
shape = (5,5)
fill  = 0
position = (1,1)

R = np.ones(shape, dtype=Z.dtype)*fill
P  = np.array(list(position)).astype(int)
Rs = np.array(list(R.shape)).astype(int)
Zs = np.array(list(Z.shape)).astype(int)

R_start = np.zeros((len(shape),)).astype(int)
R_stop  = np.array(list(shape)).astype(int)
Z_start = (P-Rs//2)
Z_stop  = (P+Rs//2)+Rs%2

R_start = (R_start - np.minimum(Z_start,0)).tolist()
Z_start = (np.maximum(Z_start,0)).tolist()
R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop-Zs,0))).tolist()
Z_stop = (np.minimum(Z_stop,Zs)).tolist()

r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]
z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]
R[r] = Z[z]
print(Z)
print(R)
```

#### 81. Consider an array Z = \[1,2,3,4,5,6,7,8,9,10,11,12,13,14\], how to generate an array R = \[\[1,2,3,4\], \[2,3,4,5\], \[3,4,5,6\], ..., \[11,12,13,14\]\]? (★★★)


```python
# Author: Stefan van der Walt

Z = np.arange(1,15,dtype=np.uint32)
R = stride_tricks.as_strided(Z,(11,4),(4,4))
print(R)
```

#### 82. Compute a matrix rank (★★★)


```python
# Author: Stefan van der Walt

Z = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(Z) # Singular Value Decomposition
rank = np.sum(S > 1e-10)
print(rank)
```

#### 83. How to find the most frequent value in an array?


```python
Z = np.random.randint(0,10,50)
print(np.bincount(Z).argmax())
```

#### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)


```python
# Author: Chris Barker

Z = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (Z.shape[0]-3)
j = 1 + (Z.shape[1]-3)
C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
print(C)
```

#### 85. Create a 2D array subclass such that Z\[i,j\] == Z\[j,i\] (★★★)


```python
# Author: Eric O. Lebigot
# Note: only works for 2d array and value setting using indices

class Symetric(np.ndarray):
    def __setitem__(self, index, value):
        i,j = index
        super(Symetric, self).__setitem__((i,j), value)
        super(Symetric, self).__setitem__((j,i), value)

def symetric(Z):
    return np.asarray(Z + Z.T - np.diag(Z.diagonal())).view(Symetric)

S = symetric(np.random.randint(0,10,(5,5)))
S[2,3] = 42
print(S)
```

#### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)


```python
# Author: Stefan van der Walt

p, n = 10, 20
M = np.ones((p,n,n))
V = np.ones((p,n,1))
S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
print(S)

# It works, because:
# M is (p,n,n)
# V is (p,n,1)
# Thus, summing over the paired axes 0 and 0 (of M and V independently),
# and 2 and 1, to remain with a (n,1) vector.
```

#### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)


```python
# Author: Robert Kern

Z = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                       np.arange(0, Z.shape[1], k), axis=1)
print(S)
```

#### 88. How to implement the Game of Life using numpy arrays? (★★★)


```python
# Author: Nicolas Rougier

def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive] = 1
    return Z

Z = np.random.randint(0,2,(50,50))
for i in range(100): Z = iterate(Z)
print(Z)
```

#### 89. How to get the n largest values of an array (★★★)


```python
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

# Slow
print (Z[np.argsort(Z)[-n:]])

# Fast
print (Z[np.argpartition(-Z,n)[:n]])
```

#### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)


```python
# Author: Stefan Van der Walt

def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)

    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]

    return ix

print (cartesian(([1, 2, 3], [4, 5], [6, 7])))
```

#### 91. How to create a record array from a regular array? (★★★)


```python
Z = np.array([("Hello", 2.5, 3),
              ("World", 3.6, 2)])
R = np.core.records.fromarrays(Z.T, 
                               names='col1, col2, col3',
                               formats = 'S8, f8, i8')
print(R)
```

#### 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)


```python
# Author: Ryan G.

x = np.random.rand(5e7)

%timeit np.power(x,3)
%timeit x*x*x
%timeit np.einsum('i,i,i->i',x,x,x)
```

#### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)


```python
# Author: Gabe Schwartz

A = np.random.randint(0,5,(8,3))
B = np.random.randint(0,5,(2,2))

C = (A[..., np.newaxis, np.newaxis] == B)
rows = np.where(C.any((3,1)).all(1))[0]
print(rows)
```

#### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. \[2,2,3\]) (★★★)


```python
# Author: Robert Kern

Z = np.random.randint(0,5,(10,3))
print(Z)
# solution for arrays of all dtypes (including string arrays and record arrays)
E = np.all(Z[:,1:] == Z[:,:-1], axis=1)
U = Z[~E]
print(U)
# soluiton for numerical arrays only, will work for any number of columns in Z
U = Z[Z.max(axis=1) != Z.min(axis=1),:]
print(U)
```

#### 95. Convert a vector of ints into a matrix binary representation (★★★)


```python
# Author: Warren Weckesser

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
B = ((I.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)
print(B[:,::-1])

# Author: Daniel T. McDonald

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
print(np.unpackbits(I[:, np.newaxis], axis=1))
```

#### 96. Given a two dimensional array, how to extract unique rows? (★★★)


```python
# Author: Jaime Fernández del Río

Z = np.random.randint(0,2,(6,3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print(uZ)
```

#### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)


```python
# Author: Alex Riley
# Make sure to read: http://ajcr.net/Basic-guide-to-einsum/

A = np.random.uniform(0,1,10)
B = np.random.uniform(0,1,10)

np.einsum('i->', A)       # np.sum(A)
np.einsum('i,i->i', A, B) # A * B
np.einsum('i,i', A, B)    # np.inner(A, B)
np.einsum('i,j->ij', A, B)    # np.outer(A, B)
```

#### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?


```python
# Author: Bas Swinckels

phi = np.arange(0, 10*np.pi, 0.1)
a = 1
x = a*phi*np.cos(phi)
y = a*phi*np.sin(phi)

dr = (np.diff(x)**2 + np.diff(y)**2)**.5 # segment lengths
r = np.zeros_like(x)
r[1:] = np.cumsum(dr)                # integrate path
r_int = np.linspace(0, r.max(), 200) # regular spaced path
x_int = np.interp(r_int, r, x)       # integrate path
y_int = np.interp(r_int, r, y)
```

#### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)


```python
# Author: Evgeni Burovski

X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                [2.0, 0.0, 1.0, 1.0],
                [1.5, 2.5, 1.0, 0.0]])
n = 4
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
M &= (X.sum(axis=-1) == n)
print(X[M])
```

#### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)


```python
# Author: Jessica B. Hamrick

X = np.random.randn(100) # random 1D array
N = 1000 # number of bootstrap samples
idx = np.random.randint(0, X.size, (N, X.size))
means = X[idx].mean(axis=1)
confint = np.percentile(means, [2.5, 97.5])
print(confint)
```

    [-0.15458016  0.25472856]

