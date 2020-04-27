##
graph = {
        "A": ["B","C"],
        "B": ["A","C","D"],
        "C": ["A","B","D","E"],
        "D": ["B","C","E","F"],
        "E": ["C","D"],
        "F": ["D"]
        }


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while len(queue)>0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)

BFS(graph, 'C')


##
def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack)>0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

BFS(graph, 'C')

##

stack = []
stack.append('A')
stack

Input = "{[]}"


class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(', '}':'{',']':'['}
        stack = []
        for i in s:
            
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if (len(stack)==0) or (d[i]!=stack.pop()):
                    return False
        return stack == []
Solution().isValid(Input)

##

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root):
        depth = 0 
        level = [root] if root else []
        print(level)
            
        

Input = [3,9,20,null,null,15,7]
a = TreeNode(3)
a.val
a.left = 9



##

Solution().maxDepth(TreeNode(Input))

##       


##

