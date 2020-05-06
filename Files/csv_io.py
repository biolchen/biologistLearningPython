Infile='test.csv'

# CHAPTER 5 Files and I/O
# 5.1. Reading and Writing Text Data
with open(Infile, 'rt') as f:
    data = f.read()
    print(data)

with open(Infile, 'rt') as f:
    for line in f:
        print (line)

print (data)





