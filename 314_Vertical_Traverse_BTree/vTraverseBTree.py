#definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
"""
class Solution(object):

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        #corner case
        if root is None:
            return []

        #hash table which column number as key and node value in 
        colHash = {}
    
        #set the root node column as 0 and dfs to get column for each node
        #self.dfsGetColumn(root, 0, colHash)

        #bfs to get column for each node 
        self.bfsGetColumn(root,colHash)
        
        #sort hash table by key (column number) in ascending order
        return [ t[1] for t in sorted(colHash.iteritems())]
    
    
    #----------------------------------------------------------------------------
    #Use Depth first search to traverse the tree, and record the column number along the way.
    #If we set the column of the tree root as 0, all the column number of child nodes that are left to the root will be negative, that are right to the root will be positive.
    #Since it is depth first search and if we record the column of current node first before recursively go to left and right child, the the value in each column will be vertical. And for two nodes in the same row and column, the order is guranteed from left to right also since it is process left branches first, then right branch.
    #Note: wrong answer, should use bfs instead of dfs
    #ex.  3
    #    / \
    #   9   4
    #    \ 
    #     8
    #      \
    #       10
    # (4) and (10) have the same column number 1, and 4 should be traversed earlier
    # than 10. However, in dfs method, 10 is traversed ealier than 4 since 10 is in 
    # left branch of root while 4 is in right branch
    #----------------------------------------------------------------------------
    def dfsGetColumn(self, node, col, hashTable): 
        """ 
        :type node: TreeNode
        :type col: int, the column number for node 
        """

        #append the current node value into hash[col] which is a list with all the node value having col as its column number
        #if the column number doesn't exist in hash yet, create a new list
        hashTable.setdefault(col, []).append(node.val)

        #go to left branch recursively
        #with current column number - 1, since its left child is one column left to the current node
        if node.left is not None:
            self.dfsGetColumn(node.left, col-1, hashTable)

        #similary to right branch
        if node.right is not None:
            self.dfsGetColumn(node.right, col+1, hashTable)
            
    
    #----------------------------------------------------------------------------
    #Use Depth first search to traverse the tree, and record the column number along the way.
    #----------------------------------------------------------------------------
    def bfsGetColumn(self, root, hashTable):
        """
        :type root: TreeNode
        :type hashTable: dictionary
        """
        #initialzie queue with root node and its colunm number
        #set the column number of root as 0
        queue = [(root, 0)]
        
        while len(queue) != 0:
            e = queue.pop(0)
            hashTable.setdefault(e[1], []).append(e[0].val)
            
            #enqueue children of current node
            if e[0].left is not None:
                queue.append((e[0].left, e[1]-1))
            if e[0].right is not None:
                queue.append((e[0].right, e[1]+1))

"""
test

myTest = Solution()

#testcase 1)
print "----------------------------------------------------------------"
print "tc1: t = [3,9,20, None, None, 15, 7] => [[9], [3,15], [20], [7]]"
t = Tree([3,9,20, None, None, 15, 7]) 
print myTest.verticalOrder(t.root)

#testcase 2)
print "----------------------------------------------------------------"
print "tc2: t = [3,9,8,4,0,1,7] => [[4],[9],[3,0,1],[8],[7]]"
t = Tree([3,9,8,4,0,1,7])
print myTest.verticalOrder(t.root)
"""
