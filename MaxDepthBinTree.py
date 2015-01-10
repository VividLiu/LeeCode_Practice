#usr/bin/python

#question:
#Given a binary tree, find its maximum depth

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
    	#None node type check
    	if root == None:
    		return 0

    	if root.left == None and root.right == None:
    		return 1
    	elif root.left != None and root.right != None:
    		mdepth = max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
    	elif root.left != None:
    		mdepth = self.maxDepth(root.left) + 1
    	else:
    		mdepth = self.maxDepth(root.right) + 1

    	return mdepth

#construct tree
rootNode = TreeNode(1)
leftNode = TreeNode(1)
rightNode = TreeNode(1)
llNode = TreeNode(1)

leftNode.left = llNode
rootNode.left = leftNode
rootNode.right = rightNode

myTree = rootNode

myTree2 = None
#test
mySolution = Solution()

print mySolution.maxDepth(myTree)



