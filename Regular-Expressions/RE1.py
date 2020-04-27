import re

emails = '''
CoreyMMSchafer@gmail.com\n
coMMMey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile('MM*')
re.findall(pattern, emails)
re.search(pattern, emails)

