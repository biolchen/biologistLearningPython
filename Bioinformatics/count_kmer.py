##

with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')
##

with open('input.txt', 'r') as file:
    data = file.read()

##

def PatternCount(Text, Pattern):
    count = 0
    for i,v in enumerate(Text):
        kmer = Text[i:i+len(Pattern)]
        if kmer == Pattern:
            count +=1  
    return count

PatternCount('TACGCATTACAAAGCACA','AA')


##
def FrequentWords(Text, k):
    """
    >>> samples = 'ATATA'
    >>> FrequentWords(samples, 2)
    ['AT', 'TA']
    """
    from collections import Counter
    most_common_kmer = []
    kmer_d = []
    for i,v in enumerate(Text):
            kmer_d.append(Text[i:i+k])
    counts = Counter(kmer_d)
    top_count = counts.most_common(1)[0][1]
    most_common_kmer = [i for i in counts if counts[i] == top_count]
    return most_common_kmer


FrequentWords('CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT', 3)
##

samples = 'GCTAGCT'

def ReverseComplement(Pattern):
    rev_comp = []
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    for i in Pattern:
        rev_comp.append(complement[i])
    return ''.join(rev_comp)[::-1]

ReverseComplement(samples)

##
P = 'AA'
G = 'TACGCATTACAAAGCACA'

def PatternMatching(Pattern, Genome):
    output_list = []
    for i,v in enumerate(Genome):
        kmer = Genome[i:i+len(Pattern)]
        if kmer == Pattern:
            output_list.append(i)
    return output_list

PatternMatching(P,G)
##


'''
Clump Finding Problem: Find patterns forming clumps in a string.

Input: A string Genome, and integers k, L, and t.

Output: All distinct k-mers forming (L, t)-clumps in Genome.
'''
##
samples = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k = 5 
l = 50 
t = 4



def ClumpFinding(genome, k, L, t):
    output = []
    from collections import defaultdict
    kmers = defaultdict(list)
    for i,v in enumerate(genome):
        input = genome[i:i+L]
        kmer = input[0:k]
        kmers[kmer].append(i)
        print(kmers)
    for i,v in kmers.items():
        if len(v) >= t:
            print(i)
            output.append(i)
    return output

ClumpFinding(samples, k,l,t)

##
def DNAtoRNA():
    import re
    re.sub('T', 'U', samples)
     
##
NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
SymbolToNumber = {'A':0, 'C':1, 'G':2, 'T':3}

def NumberToPattern2(n, k):
    pattern = [NumberToSymbol[0] for el in range(k)]
    for i in range(k - 1, -1, -1):
        pattern[i]= NumberToSymbol[n % 4]
        n /= 4
    return ''.join(pattern)
    
def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol[index]
    prefixIndex = int(index / 4)
    r = index % 4
    prefixPattern = NumberToPattern(prefixIndex, k - 1)
    return prefixPattern + NumberToSymbol[r]


##
def PatternToNumber(pattern):
    if len(pattern)  == 0:
        return 0
    return 4 * PatternToNumber(pattern[:-1]) + SymbolToNumber[pattern[-1]]
##

###
p='TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC '
q='GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'


def HammingDistance(p, q):
    output = 0
    for i in zip(p,q):
        if i[0] != i[1]:
            output += 1
    return output

HammingDistance(p,q)

###
a = 'ATTCTGGA'
b = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
d = 3

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    for i,v in enumerate(Text):
        kmer = Text[i:i+len(Pattern)]
        if len(kmer)==len(Pattern):
            count = 0
            for j in zip(kmer, Pattern):
                if j[0] != j[1]:
                    count += 1
            if count <= d:
                positions.append(i)
    return positions
        
ApproximatePatternMatching(b, a, d)

##

def ApproximatePatternCount(Text, Pattern, d):
    positions = [] # initializing list of positions
    for i,v in enumerate(Text):
        kmer = Text[i:i+len(Pattern)]
        if len(kmer)==len(Pattern):
            count = 0
            for j in zip(kmer, Pattern):
                if j[0] != j[1]:
                    count += 1
            if count <= d:
                positions.append(i)
    return len(positions)

##
Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4 
d = 1

def FrequentWordsWithMismatches(Text, k, d):
    output = []
    kmer_list = []
    for i,v in enumerate(Text):
        kmer = Text[i:i+k]
        if len(kmer) == 4:
            kmer_list.append(kmer)
    mismatch_count = 0
    for j in kmer_list:
        for i,v in enumerate(Text):
            kmer = Text[i:i+k]
            if len(kmer)==4:
                count = sum(c1!=c2 for c1,c2 in zip(Text[i:i+4],j))
                if count >= mismatch_count:
                    output.append(j) 
    return output

FrequentWordsWithMismatches(Text, k, d)
    
##
pattern = 'ACG'
d = 1

def HammingDistance(p, q):
    """ 
    input: Two strs of equal length
    return: Int: the number of positions at which the corresponding symbols are different
    """
    output = 0
    for i in zip(p,q):
        if i[0] != i[1]:
            output += 1
    return output

HammingDistance('CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA', 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG')

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

Neighbors('ACGT', 1)
##

def FrequentWordsWithMismatches(Text, k, d):
    """ Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
    Input: str, int: k and d
    Output: All most frequent k-mers with up to d mismatches in Text.
    """
    Patterns = {}
    Close = {}

    for i in range(0, 4**k):
        Close[i] = 0
    for i in range(0, len(Text)-k+1):
        Neighborhood = Neighbors(Text[i:i+k], d)
        for Pattern in Neighborhood:
            index = patternToNumber(Pattern)
            Close[index] += 1 
            Patterns[Pattern] = index
    maxCount = max(Close.values())
    return Close, Patterns

FrequentWordsWithMismatches('ACGT', 2, 1)

##
def symbolToNumber(symbol):
    if symbol == "A":
        number = 0
    elif symbol == "C":
        number = 1
    elif symbol == "G":
        number = 2
    elif symbol == "T":
        number = 3
    return number

def patternToNumber(Pattern):
    patternList = list(Pattern)
    if not patternList:
        return 0
    symbol = patternList[-1]
    prefix = patternList[:-1]
    result = 4 * patternToNumber(prefix) + symbolToNumber(symbol)
    return result

patternToNumber('TC')



patternToNumber('TACGATCGTATA')

def ComputingFrequencies(Text, k):
    import numpy as np
    k = int(k)
    FrequencyArray = np.zeros(4**k, dtype='int64')
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        index = patternToNumber(Pattern)
        FrequencyArray[index] += 1
    return FrequencyArray

ComputingFrequencies('TCGA', 2)
##


FrequentWordsWithMismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4,1)

##
# Week2
def MinimumSkew(Genome):
    """
    return: a list in indices
    """
    import numpy as np
    a = np.zeros(len(Genome)+1)
    cntr = 0
    for i,v in enumerate(Genome):
        if v == 'C':
            cntr -= 1
        if v == "G":
            cntr += 1
        a[i+1]=cntr
    output = np.where(a == a.min())
    return output[0].tolist()

MinimumSkew('GATACACTTCCCGAGTAGGTACTG')
##



##


def findMismatches(kmer, test):
    mismatches = 0
    for i in range(len(kmer)-len(kmer)):
        if kmer[i]!= test[i]:
            mismatches += 1
    return mismatches

def sharedMotif(Dna, kmer, d):
    shared = False
    shares = 0
    for seq in Dna:
        found = False
        for i in range(len(seq) - len(kmer)):
            test = seq[i:i+len(kmer)]
            if findMismatches(kmer, test) <= d:
                found = True
                shares += 1
                break
        if found == False:
            break
    if shares == len(Dna):
        shared = True
    return shared

def MotifEnumeration(Dna, k, d):
    patterns = []
    for seq in Dna:
        #Checks each kmer in a sequence
        for i in range(len(seq)-k):
            pattern = seq[i:i+k]
            #Checks kmer against each kmer in a sequence for mismatches
            for j in range(len(seq)-k):
                test = seq[j:j+k]
                mismatches = findMismatches(pattern, test)
                if mismatches <= d:
                    if sharedMotif(Dna, test, d) == True:
                        if test not in patterns:
                            patterns.append(test)
    return patterns
input_dna
MotifEnumeration(input_dna, 3, 1)
##

input_dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']

def MotifEnumeration(Dna, k, d):
    k = int(k)
    d = int(d)
    Neighborhoods = [[] for i in range(len(Dna))]
    print(Neighborhoods)
    for i in range(len(Dna)):
        Text = Dna[i]
        for j in range(len(Text)-k+1):
            if d == 0:
                Neighborhoods[i].append(Text[j:j+k])
            else:
                for z in Neighbors(Text[j:j+k],d):
                    Neighborhoods[i].append(z)
    result = set(Neighborhoods[0])
    print(result)
    print(Neighborhoods[1:])
    for s in Neighborhoods[1:]:
        result.intersection_update(s)
    return list(result)

MotifEnumeration(input_dna, 3, 1)
##

