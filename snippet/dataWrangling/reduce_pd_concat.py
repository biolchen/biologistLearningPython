from functools import reduce
d1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
d2 = pd.DataFrame({'col1': [4, 5], 'col2': [6, 7]})
d3 = pd.DataFrame({'col1': [9, 5], 'col2': [6, 1]})

pd.concat([d1,d2], axis=0)

l = [d1,d2,d3]
df = reduce(lambda x,y: pd.concat([x,y], axis=0), l)