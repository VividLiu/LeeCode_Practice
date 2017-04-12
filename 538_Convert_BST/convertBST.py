#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Use DFS algrithm
Travering the tree in (right, root, left) order, so the output sequence will be in descending order. If we use a global variable 'acum' to store the sum of node value traversed so far. The transformed value of current node should be val = val + acum since acum is the sum of all nodes that are greater than the current one, thanks to the descending order traverse
Ex.
        8
       /  \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

The dfs traversing order will be: 
    14, 13, 10, 8,  7,  6,  4,  3,  1
The global acum value will be:
    0,  14, 27, 37, 45, 52, 58, 62, 65, 66
"""
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.Xdfs(root)

        return root


    # tree: tree node to be traversed
    # acum: store the sum of travered node so far, thus it has to be global variable
    # the transfromed node value will be val = val + acum, since acum is the accumulated sum of all node that are greater than the current one
    __acum = 0
    def Xdfs(self, tree):
        if tree is None:
            return 0

        if(tree.right):
            self.Xdfs(tree.right)


        #transform current root value
        tree.val += self.__acum
        #
        self.__acum = tree.val

        if(tree.left):
            self.Xdfs(tree.left)
