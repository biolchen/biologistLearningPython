##
def HammingDistance(p, q):
    output = 0
    for i in zip(p,q):
        if i[0] != i[1]:
            output += 1
    return output

def Neighbors(Pattern, d):
    prefix = Pattern[0]
    suffix = Pattern[1:len(Pattern)]
    if d == 0:
        return ([Pattern])
    if len(Pattern) == 1:
        return (['A', 'C', 'G', 'T'])
    SuffixNeighbors = Neighbors(suffix, d)

    Neighborhood = []
    for Text in (SuffixNeighbors):
        if HammingDistance(suffix, Text) < d:
            for base in "ACGT":
                Neighborhood.append(base + Text)
        else:
            Neighborhood.append(prefix + Text)
    return (Neighborhood)

def MotifEnumeration(Dna, k, d):
    k = int(k)
    d = int(d)
    Neighborhoods = [[] for i in range(len(Dna))]
    for i in range(len(Dna)):
        Text = Dna[i]
        for j in range(len(Text)-k+1):
            if d == 0:
                Neighborhoods[i].append(Text[j:j+k])
            else:
                for z in Neighbors(Text[j:j+k],d):
                    Neighborhoods[i].append(z)
    result = set(Neighborhoods[0])
    for s in Neighborhoods[1:]:
        result.intersection_update(s)
    return list(result)

##

Neighbors('ACGT', 1)


input_dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
MotifEnumeration(input_dna, 3, 1)
##
