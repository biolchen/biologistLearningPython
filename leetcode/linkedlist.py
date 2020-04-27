##
class Node:
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class NewList:
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print('')

    def add(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp

        else:
            temp.next = self.head
            self.head = temp
            print('')


    def append(self, item):
        temp = Node(item)
        origin = self.head
        if self.head is None:
            self.head = temp
        else:
            while origin.next is not None:
                origin = origin.next

            else:
                origin.next = temp

    def serach 
