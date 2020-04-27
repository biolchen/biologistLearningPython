def get_list_from_txt(input_list_f):
    """a function to read txt file line-by-line into a list
    """
    f=open(input_list_f, 'r')
    output_list=[line.rstrip('\n') for line in f]
    f.close()
    return output_list