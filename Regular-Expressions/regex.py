##
##
import math
##
import re

example = "Welcome to the world of Python"
pattern = r'Python'
match = re.search(pattern, example)
match.group()
##
re.match(r'^\d{3}\-\d{3,6}$', '010-12345')

##
# match()方法判断是否匹配，
##如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：


##
def test_match(s):
    test = 'whatever'
    if re.match(s, test):
        print(re.match(s, test))
        print('ok')
    else:
        print('failed')


test_match('whatever')
##
match.end()
dir(re.search)


pattern = re.compile(r'hello')
a = re.match(pattern, 'hello world')
b = re.search(pattern, 'world hello')
b2 = re.match(pattern, 'world hello')
c = re.match(pattern, 'hell')
d = re.match(pattern, 'hello ')
##
if a:
    print("a: {}".format(a.group()))
else:
    print('a 失败')
if b:
    print("b: {}".format(b.group()))
else:
    print('b: 失败')
if b2:
    print("b2: {}".format(b2.group()))
else:
    print('b2: fail')
if c:
    print(c.group())
else:
    print('c: 失败')
if d:
    print("d: {}".format(d.group()))
else:
    print('d: 失败')
##
print("a\n\na")
print(r"a\n\na")


##
def test_function(text):
    print(text)


##
test_function("ddd")


def drone():
    print("dddd")


drone()
##
x = range(0, 10)


def test_cube(num):
    new_list = []
    for i in num:
        new_list.append(i**3)
    return new_list


test_cube(x)
print(list(map(math.exp, x)))


## filters
def divis_by_2(num):
    return num % 2 == 0


list(map(divis_by_2, x))
list(filter(divis_by_2, x))


def has_2x(my_string):
    return my_string.count("x") >= 2


y = ["xy", "xxxx"]

list(filter(has_2x, y))

"xxxx".count("x")

text = 'asdaf fadf; afed, fea,adfa,    foo'
re.split(r'[;,\s]\s*', text)  #good output
re.split(r'(;|,|\s)|\s*', text)
p = re.compile('[a-z]+')
re.compile('[a-z]+')
