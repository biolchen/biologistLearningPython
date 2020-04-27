##
def find_index(to_search, target):
  for i, value in enumerate(to_search):
    if value == target:
      print(value)
  else:
    return -1
  return i
##
my_list = ['Corey', 'Rick', 'John', 'Steve']
find_index(my_list, 'Steve')
find_index(my_list, 'Jimmy')
##
