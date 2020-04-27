import os
def oswalk(dir):
    print("print files")
    files=[]
    dirs=[]
    indir = dir
    for root, dirs, file in os.walk(indir):
        files = [f for f in file if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        return files