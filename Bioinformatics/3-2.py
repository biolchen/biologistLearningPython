##
class MedianString:
    """
    Input:  k, followed by a collection of strings Dna
    Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern. 
    """
    def __init__(self, k, dna_list):
        self.k = int(k)
        self.dna_list = dna_list

    def main(self):
        for i in range(len(self.dna_list)):
            dna = self.dna_list(i)
       
    def NumberToSymbol(self, index):
        index = int(index)
        if index == 0:
            return 'A'
        elif index == 1:
            return 'C'
        elif index == 2:
            return 'G'
        elif index == 3:
            return 'T'

    def NumberToPattern(self, index, k):
        index = int(index)
        k = int(k)
        if k == 1:
            return self.NumberToSymbol(index)
        else:
            prefixIndex = index//4
            r = index%4
            symbol = self.NumberToSymbol(r)
            return self.NumberToPattern(prefixIndex,k-1) + symbol
 
    def get_kmers(self, dna, d):
        kmers = []
        for j in range(len(dna)-self.k+1):
                if d == 0:
                    kmers.append(dna[j:j + self.k])
                else:
                    for z in self.Neighbors(dna[j:j + self.k], d):
                        kmers.append(z)
        return kmers
    
    def get_kmers_distance(self, dna, d):
        d = {}
        for i in self.get_kmers(dna, d):
            d[i] = self.HammingDistance(i, self.dna)
        return d
   
    def HammingDistance(self, p, q):
        output = 0
        for i in zip(p,q):
            if i[0] != i[1]:
                output += 1
        return output
    
    def DistanceBetweenPatternAndStrings(self, Pattern, Dna):
        k = len(Pattern)
        distance = 0
        for Text in Dna:
            hammingDistance = float("inf")
            for i in range(len(Text)-k+1):
                if hammingDistance > self.HammingDistance(Pattern, Text[i:i+k]):
                    hammingDistance = self.HammingDistance(Pattern, Text[i:i+k])
            distance += hammingDistance
        return distance

    def MedianString(self, Dna, k):
        k = int(k)
        distance = float('inf')
        for i in range(4**k):
            Pattern = self.NumberToPattern(i,k)
            if distance > self.DistanceBetweenPatternAndStrings(Pattern, Dna):
                distance = self.DistanceBetweenPatternAndStrings(Pattern, Dna)
                Median = Pattern
        return Median
 
    def Neighbors(self,Pattern, d):
        prefix = Pattern[0]
        suffix = Pattern[1:len(Pattern)]
        if d == 0:
            return ([Pattern])
        if len(Pattern) == 1:
            return (['A', 'C', 'G', 'T'])
        SuffixNeighbors = self.Neighbors(suffix, d)
        Neighborhood = []
        for Text in (SuffixNeighbors):
            if self.HammingDistance(suffix, Text) < d:
                for base in "ACGT":
                    Neighborhood.append(base + Text)
            else:
                Neighborhood.append(prefix + Text)
        return (Neighborhood)


##
dnas = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
k=3
d=1
a = MedianString(3, dnas)
a.HammingDistance('AA','ATCG')
a.Neighbors('ACT',1)
a.get_kmers(dnas[0], 1)
a.get_kmers_distance(dnas[0], 1)
a.DistanceBetweenPatternAndStrings(Pattern='ATC', Dna = ['ATAATC', 'GGGGGGC','AAAAATT'])
a.MedianString(dnas, 3)
##
