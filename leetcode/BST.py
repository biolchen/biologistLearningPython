##

class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value already in tree!')

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print("{}".format(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

def fill_tree(tree,num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

##
root = [10,5,15,3,7,18]
L = 7
R = 15
##
tree=BST()
for i in root:
    tree.insert(i)
##
tree.print_tree()

tree=fill_tree(tree)
tree.print_tree()
##

a = [-1,4,2,3]



##
##
COUNT = [10]
class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
##
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)

root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

root.left.left.left = newNode(8)
root.left.left.right = newNode(9)
root.left.right.left = newNode(10)
root.left.right.right = newNode(11)
root.right.left.left = newNode(12)
root.right.left.right = newNode(13)
root.right.right.left = newNode(14)
root.right.right.right = newNode(15)

print2D(root)
##
Input = [17,13,11,2,3,5,7]
Input=sorted(Input,reverse=True)
dp = []
print(Input)
for i in Input:
    dp = [i] +  dp[-1:]+dp[:-1]
    print(dp)
    
##
Input = [17,13,11,2,3,5,7]
class Solution:
        def deckRevealedIncreasing(self, deck):
            deck.sort(reverse=True)
            dp = []
            for i in deck:
                dp = [i] + dp[-1:]+dp[:-1]
            return dp 

Solution().deckRevealedIncreasing(Input)
##


words = ["abc","deq","mee","aqq","dkd","ccc"]
##
pattern = "abb"
m = {}
for i in pattern:
    print(m.setdefault(i, len(m)))
print(m)
##

dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" %  dict.setdefault('Age', None))
print("Value : %s" %  dict.setdefault('Sex', None))
##
class Solution:
    def F(self,w):
        m={}
        return [m.setdefault(c,len(m)) for c in w]

Solution().F("maa")
##


        def findAndReplacePattern(self, words, pattern):
            





