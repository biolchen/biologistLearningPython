import numpy as np

np.zeros([3,2])

np.diag([3,2,5])

np.arange(90)

np.meshgrid([10,1,1],[1,1,1])

np.meshgrid
np.ones([4,4])
np.empty([4,444])
np.arange(0, 10, 1)


np.linspace(0,10,11)


np.logspace(0, 2, 5)


x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])
X, Y = np.meshgrid(x, y)

X
Y

np.empty(3, dtype=np.int64)


import re
pattern = re.compile(r'\bfoo\b')
a = pattern.match("foo bar")
a.group()


pattern = re.compile("\\\\")
pattern.match("\\author").group()

pattern = re.compile(r'world')
pattern.findall("hello world")
a = pattern.search("hello world")
a.group()



