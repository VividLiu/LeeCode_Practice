#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
If a node is BST, it has to satisfy the following criteria:
1). Its left child node.left (if it exists) is also a BST
2). Its right child node.right (if it exists) is also a BST
Note: only satisfying these two won't guarantee it is a BST.
Ex.     5
       / \
      3   6
     / \
    1   7
the left subtree is also a BST, but 7 > 5 which makes the root not BST.
Thus, in addition to the two criteria above, it has to satisfy the folloing criteria also:
3). The maximum value in its left substree must be smaller than node.val
4). The minimum value in its right subtree must be larger than node.val

Solution:
Use dfs to recursivly check the validation of its left child and right child and compare the minimum value in left subtree and the maximum value in right subtree.
The minimum and maximum value of a tree can be updated along the dfs recursively also.
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minval, maxval = 0, 0
        
        return self.helper(root, minval, maxval)
        
    #return if root is a valid bst tree
    #and pass back the minimal and maximal value in tree
    def helper(self, node, minmax):
        """
        :type node: TreeNode
        :type minmax: list[int], where len = 2.
                      list[0]: minimal value in node
                      list[1]: maximal value in node
        """
        #leaf node, valid bst 
        if not node.left and not node.right:
            minmax[0] = minmax[1] = node.val
            return True
        
        #return bool result
        valid = True
        
        #the minimal & maximul value in left and right child of node separately
        lminmax = [0, 0]
        rminmax = [0, 0]
        
        #initialize minVal, maxVal
        minmax[0] = minmax[1] = node.val
        
        if node.left:
            valid &= self.helper(node.left, lminmax)
            valid &= (lminmax[1] < node.val)
            minmax[0] = lminmax[0]
            
        if node.right:
            valid &= self.helper(node.right,rminmax)
            valid &= (rminmax[0] < node.val)
            minmax[1] = rminmax[1]
        
        return valid
        
        
