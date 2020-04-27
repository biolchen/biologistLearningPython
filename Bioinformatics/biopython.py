##

import os
from Bio import SeqIO
os.chdir(os.path.dirname(__file__))
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
	print(seq_record.id)
##

from reprlib import recursive_repr
class MyList(list):
    @recursive_repr()
    def __repr__(self):
        return '<' + '|'.join(map(repr, self)) + '>'

m = MyList('abc')
m.append(m)
m.append('x')
print(m)

##
from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print(my_seq)
##
Seq('AGTACACTGGT', Alphabet())
print(my_seq)
##
from Bio import Entrez
Entrez.email="biolchen@gmail.com"

##
from biokit.sequence.benchmark import SequenceBenchmark

def create_sequence(expectedLength=1e6):
    s = SequenceBenchmark()
    return s.create_sequence(expectedLength)
sequence = create_sequence(1e7)    
##
# Create some random data
import string
letters = string.ascii_uppercase[0:15]
import pandas as pd
import numpy as np
df = pd.DataFrame(dict(( (k, np.random.random(10)+ord(k)-65) for k in letters)))
df = df.corr()

# if the input is not a square matrix or indices do not match 
# column names, correlation is computed on the fly
from biokit.viz import corrplot
c = corrplot.Corrplot(df)


c.plot(colorbar=False, method='square', shrink=.9 ,rotation=45)
##
