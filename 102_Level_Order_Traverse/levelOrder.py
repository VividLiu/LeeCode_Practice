#Defition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Solution: 
BFS
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #sanity check
        if not root:
            return []

        #initialize bfs queue
        #e = (node, level)
        queue = [(root,0)]

        #return result
        res = []

        while queue:
            x, l = queue.pop(0)
            
            if x.left:
                queue.append((x.left, l+1)) 
            if x.right:
                queue.append((x.right, l+1)) 

            #this level already exist, append more
            if l < len(res):
                res[l].append(x.val)
            else: #new level
                res.append([x.val]) 

        return res
