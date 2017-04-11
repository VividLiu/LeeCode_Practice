#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
BFS algorithm
Enque (node, level) pair into the bfs queue for each node. 
node is the current tree node, level is the depth for the node.
Thus, when we pop out the node from queue, we have its depth info.
For each depth, just has a value to record the maximum value, 
and start fresh recording when encounter the next depth.
"""
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
            
        #return list
        rlist = [] 
        
        #variable defintion
        m = root.val #max number for each level
        #Note: since node value can be negative, m can not be initialized
        # as 0. Should be initialized as the first root value

        d = 0 #current depth
        
        #put the root node into queue 
        queue = [(root, 0)]
        
        while(queue):
            #pop the top element from queue
            e = queue.pop(0)
            
            #enque the child nodes
            if(e[0].left):
                queue.append((e[0].left, e[1]+1))
            if(e[0].right):
                queue.append((e[0].right, e[1]+1))
            
            #update maximum number 
            if(e[1] != d):  #entering next level, output the max value for previous and level and clear m value
                rlist.append(m)
                m = e[0].val
                d = e[1]
            else:
                if e[0].val > m:
                    m = e[0].val
            
        #append the max value for last level
        rlist.append(m)
            
        return rlist
                
                
