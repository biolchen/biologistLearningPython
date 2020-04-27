#!/Users/liangchen/Dropbox/REPO/env/DS/bin/python

import sys
import plotly
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-i', nargs='+')
args = parser.parse_args()
a=input('')
b=input('')
print("line1:{}".format(a))
print('-'*19)
print("line2:{}".format(b))
print(args.i)


if __name__ == "__main__":
    print(sys.argv)
