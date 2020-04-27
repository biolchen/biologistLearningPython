#!/usr/bin/env python
from natsort import natsorted, ns
a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
print(sorted(a))
print(natsorted(a))
##
a = ['1.2', '1.2rc1', '1.2beta2', '1.2beta1', '1.2alpha', '1.2.1', '1.1', '1.3']
natsorted(a)
natsorted(a, key=lambda x: x.replace('.', '~'))
natsorted(a, key=lambda x: x.replace('.', '~')+'z')

a = ['./folder/file (1).txt',
     './folder/file.txt',
     './folder (1)/file.txt',
     './folder (10)/file.txt']
natsorted(a)
natsorted(a, alg=ns.PATH)

from natsort import humansorted
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
a = ['Apple', 'corn', 'Corn', 'Banana', 'apple', 'banana']
natsorted(a, alg=ns.LOCALE)
humansorted(a)

a = ['Apple', 'corn', 'Corn', 'Banana', 'apple', 'banana']
natsorted(a)
natsorted(a, alg=ns.IGNORECASE)
natsorted(a, alg=ns.LOWERCASEFIRST)
natsorted(a, alg=ns.GROUPLETTERS)
natsorted(a, alg=ns.G | ns.LF)

a = ['a50', 'a51.', 'a+50.4', 'a5.034e1', 'a+50.300']
natsorted(a, alg=ns.FLOAT)
natsorted(a, alg=ns.FLOAT | ns.SIGNED)
natsorted(a, alg=ns.FLOAT | ns.SIGNED | ns.NOEXP)
natsorted(a, alg=ns.REAL)
from natsort import realsorted
realsorted(a)

from operator import attrgetter, itemgetter
a = [['a', 'num4'], ['b', 'num8'], ['c', 'num2']]
natsorted(a, key=itemgetter(1))

class Foo:
   def __init__(self, bar):
       self.bar = bar
   def __repr__(self):
       return "Foo('{0}')".format(self.bar)
b = [Foo('num3'), Foo('num5'), Foo('num2')]
natsorted(b, key=attrgetter('bar'))

from natsort import natsort_keygen
a = ['a50', 'a51.', 'a50.4', 'a5.034e1', 'a50.300']
natsort_key = natsort_keygen(alg=ns.FLOAT)
a.sort(key=natsort_key)
a

from natsort import index_natsorted, order_by_index
a = ['a2', 'a9', 'a1', 'a4', 'a10']
b = [4,    5,    6,    7,    8]
c = ['hi', 'lo', 'ah', 'do', 'up']
index = index_natsorted(a)
order_by_index(a, index)
order_by_index(b, index)
order_by_index(c, index)

a = ['a2', 'a9', 'a1', 'a4', 'a10']
natsorted(a, reverse=True)

from natsort import as_ascii
a = [b'a', 14.0, 'b']
natsorted(a, key=as_ascii) == [14.0, b'a', 'b']

from natsort import as_utf8
a = [b'a56', b'a5', b'a6', b'a40']
natsorted(a)  # doctest: +SKIP
natsorted(a, key=as_utf8) == [b'a5', b'a6', b'a40', b'a56']

from natsort import decoder
a = [b'a56', b'a5', b'a6', b'a40']
natsorted(a, key=decoder('latin1')) == [b'a5', b'a6', b'a40', b'a56']


a=[1,2,3,4,5]
b=sorted(a, key=lambda x: x, reverse=True)
b

sorted(a, key=lambda x: x[0], reverse=True)

