"""
Solution:
It is a specific case of 236. Lowest common ancestor of a binary tree.
Since it is a binary search tree, we can utilize the information of binary search tree which is the right subtree always contains values that are larger than root value; the left subtree always contains values that are smaller than root value.
Consider the following situations while searching from root:
1). When one of p.val and q.val is smaller than root.val and the other is larger than root.val; that is p and q are on the different sides of root. root must be their lowest common ancestor
2). When p and q are on the same side of root, recursively search that subtree
3). When root is equal to p or q, the lowest common ancestor must be root itself if the other node exists; othewise no common ancestor exists
"""
        
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        
        if p.val == root.val:
            return root if self.hasNode(root, q) else None
        
        if q.val == root.val:
            return root if self.hasNode(root, p) else None
        
        #using xor to test if p and q are in different side of root
        #if p and q are in different side of  root
        if (p.val < root.val) ^ (q.val < root.val): 
            if self.hasNode(root, p) and self.hasNode(root, q):
                return root
            #return root if (self.hasNode(root, p)  and self.hasNode(root, q)) else None
        elif p.val < root.val: #p and q are in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        else: #p an q are in right subtree:
            return self.lowestCommonAncestor(root.right, p, q)

    # traverse tree to find if node x is in tree root
    # @param root: TreeNode
    # @param x   : TreeNode
    # @return param: Boolean
    def hasNode(self, root, x):
        if not root:
            return False
        elif x.val == root.val:
            return True
        elif x.val < root.val:
            return self.hasNode(root.left, x)
        else:
            return self.hasNode(root.right, x)
            
"""
test
node6 = TreeNode(6)
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1)

node5.right = node6
node5.left  = node3
node3.right = node4
node3.left  = node2
node2.left  = node1

myTest = Solution()
print myTest.lowestCommonAncestor(node5, node1, node4)
"""
