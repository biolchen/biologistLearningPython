import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--ints1', metavar='N1', nargs='+')
parser.add_argument('--ints2', metavar='N2', nargs='+')
args = parser.parse_args()

print(args.ints1)
print(args.ints2)
