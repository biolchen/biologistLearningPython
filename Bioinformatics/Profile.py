
##
def Profile(motifs):
    Matrix = [[1. for i in range(len(motifs[0]))] for i in range(4)]
    for i in range(len(motifs)):
        for j in range(len(motifs[i])):
            if len(motifs[0]) == 1:
                last = i
            else:
                last = j
            if motifs[i][j] == 'A':
                Matrix[0][last] += 1
            elif motifs[i][j] == 'C':
                Matrix[1][last] += 1
            elif motifs[i][j] == 'G':
                Matrix[2][last] += 1
            elif motifs[i][j] == 'T':
                Matrix[3][last] += 1
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            Matrix[i][j] /= (len(motifs)+4)
    return Matrix

##
res = Profile(['ACTGAAAACTGTA'])
print(res)




