## 5.16. Adding or Changing the Encoding of an Already Open File

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(text)

# Example of writing raw bytes on a file opened in text mode

import sys

# A byte string
data = b'Hello World\n'

# Write onto the buffer attribute (bypassing text encoding)
sys.stdout.buffer.write(data)
from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print("Got connection from", addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

if __name__ == '__main__':
    print('Echo serving running on localhost:25000')
    echo_server(('', 25000))
# Some examples of reading text files with different options
#
# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings (\r\n).

# (a) Reading a basic text file (UTF-8 default encoding)

print("Reading a simple text file (UTF-8)")
with open('sample.txt', 'rt') as f:
    for line in f:
        print(repr(line))

# (b) Reading a text file with universal newlines turned off
print("Reading text file with universal newlines off")
with open(Infile, 'rt', newline='') as f:
    for line in f:
        print(repr(line))

# (c) Reading text file as ASCII with replacement error handling
print("Reading text as ASCII with replacement error handling")
with open('sample.txt', 'rt', encoding='ascii', errors='replace') as f:
    for line in f:
        print(repr(line))

# (d) Reading text file as ASCII with ignore error handling
print("Reading text as ASCII with ignore error handling")
with open('sample.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(repr(line))

# Example of getting a directory listing

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for r in name_sz_date:
    print(r)

# Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
# Example of iterating of fixed-size records
#
# The file 'data.bin' contains 32-byte fixed size records
# that consist of a 4-digit number followed by a 28-byte string.

from functools import partial
RECORD_SIZE = 32

with open('data.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
