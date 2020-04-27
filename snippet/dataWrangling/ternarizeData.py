a  = np.zeros((2,3))
a1 = np.zeros((2,3))
a2 = np.zeros((2,3))

b=np.array([[1,2,3],[3,1,2]])
print("a:{}".format(a))
print("b:{}".format(b))

for feature in range(a.shape[1]):
    a1[:,feature] = b[:,feature]>2
    a2[:,feature] = b[:,feature]<2
a=a+a1
a=a-a2
a=a+2

print(a)
