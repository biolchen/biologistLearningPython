import sys
from contextlib import redirect_stdout as ro
 
log_frile=open('run.out','w')

with ro(log_frile):
  print('test')
  print('*' * 40)
  
log_file.close()