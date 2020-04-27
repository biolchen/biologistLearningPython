import itertools

my_list = [1,2,3]

permutations = itertools.permutations(my_list, 2)
for p in permutations:
    print(p)