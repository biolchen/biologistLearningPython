##
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-5555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
##
#pattern = re.compile('ABC', re.I)
pattern = re.compile('\D')
a=pattern.findall(text_to_search)

a

b=pattern.finditer(text_to_search)
for i in b:
    print(type(i))
    print(i.start(), i.group(0))


##

a = re.search(r"r[a-z]n", "dog runs to cat")
a = re.search(r"\d", "dog runs to 3 cat")
a.group()



a=re.search(r"ab{2,10}", "abbbbb")
a.group()

##
c=re.compile('(5{2}),(0{2})')
output=c.search(text_to_search)
output.group()
c.findall(text_to_search)
##
import re
re.split(r'\b', 'Words, words, words.')


ie.split(r'\b', 'Words, words, words.')

line = "Cats are smarter than dogs";

s = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)


s.group()
##
