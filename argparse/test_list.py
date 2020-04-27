import argparse
import sys

parser = argparse.ArgumentParser(prog='test the argument', usage='try me', description='yeah', epilog='''
        what are you talking about?
        are you mad?
        ''')
print(parser)
parser.add_argument('-i', type=str, help='just type a string')
args = parser.parse_args(sys.argv[1:])
print(args)
print(args.i)


