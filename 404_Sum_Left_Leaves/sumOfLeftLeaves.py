# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Use bfs
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #sanity check
        if not root:
            return 0
        #(node, side) pair, side == 0: node is a left child; side == 1, node is a right child
        queue = [(root,-1)]
        leftSum = 0
        while queue:
            node, side = queue.pop(0)

            if not node.left and not node.right and side == 0: #left child
                leftSum += node.val
            if node.left:
                queue.append((node.left, 0))
            if node.right:
                queue.append((node.right, 1))
        
        return leftSum
        
