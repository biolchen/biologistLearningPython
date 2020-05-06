with open('test.txt', 'wt') as f:
    f.write("test1.tmp")
    f.write("test2.tmp")
##
with open('test.txt', 'wt') as f:
    print("line2", file=f)
    print("line3", file=f)
##
f = open('test.txt', 'rt')
data = f.read()
print(data)
f.close()