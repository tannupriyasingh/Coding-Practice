"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class preorderSolution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        listOfNodes = list()
        
        def arrangeNodes(node):
           listOfNodes.add(node) 
           for childNodes in node.children:
                  arrangeNodes(childNodes)
        
        if root:
            arrangeNodes(root)
        
        return listOfNodes
                  