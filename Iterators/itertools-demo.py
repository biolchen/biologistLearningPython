from itertools import groupby
a = 'aaaba'
list(groupby(a))


##
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
##
