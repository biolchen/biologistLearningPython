## Printing with a Different Separator or Line Ending
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

row = ('ACME', 50, 91.5)
print(','.join(str(x) for x in row))
print(*row, sep=',')