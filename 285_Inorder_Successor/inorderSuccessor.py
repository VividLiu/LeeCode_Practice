#Defition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Since it is a BST, from the feature of BST we know, the value of next in-order successor of node p will be the smallest value which is larger than p.val
Ex. the array represenstation of a BST [1, 2, 3, 4, 5]
    The next in-order successor of node 3 will be node 4, since in-order traverse of BST gives sorted list
Thus, we can use in-order traverse to get the flatten sorted list of this BST and find the value of P's successor in array. 
Then traverse the tree again to find the node with that value.

Time complexity: O(n)
two times tree traversal takes O(2n) time, and to find the value in array takes O(n) time
"""
class Solution2(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        treelist = []
        
        self.dfs(root, treelist)
        
        print treelist
        
        #find val of p in the list and the value of its next element
        sVal = None #the value of p's successor
        for i in xrange(len(treelist)):
            if p.val == treelist[i] and i < len(treelist)-1:
                sVal = treelist[i+1]
                break
                
        print sVal
        
        #find the node with sVal in tree
        if sVal != None:
            return self.findNode(root, sVal)
        else:
            return None
        
        
        
    
    #find the node with target value in tree and return that node, return None if no such node exists
    def findNode(self, root, target):
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            e = queue.pop(0)
            
            if e.val == target:
                return e
            
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
                             
        return None    
            
        
    #traverse tree using in-order dfs and output the traversed node in list
    def dfs(self, node, treeList):
        """
        :type root:        TreeNode
        :type treeList:    List[val], flattened tree as list
        """
    
        if not node:
            return []
        
        if node.left:
            self.dfs(node.left, treeList)
        
        treeList.append(node.val)
        
        if node.right:
            self.dfs(node.right, treeList)
        
        
"""
The above solution only works for BST tree. Here is the solution for gneral Binary Tree.
In normal dfs, we can use a stack to do pre-order traverse. Here, we do a little modification and use a stack to do a in-order traverse.
Instead of only pushing node into the stack, we push [node, is_left_visited] into the stack. 
When a node is first pushed into the stack, its is_left_visited flag is set to 0. 
When we pop out a node and its is_left_visited is set to 0, we push its left node, the current node, and its right node into stack in order, and set the is_left_visited of current node to 1 
When a node's left and right child are pushed into stack, its is_left_visited_flag is set to 1, which means we already visited its left branch.
When we pop out a node and its is_left_visited is set to 1, we know we already visited its left child, thus output the current node.
Then proceed.

Using the above method, we can do a in-order traverse and find the successor while traversing

Time complexity: O(n)
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        
        stack = [[root, 0]]
        
        found = 0 #flag to signal if p node has been found in traversing
        
        while stack:
            top = stack.pop(0)
            
            if top[1] == 0: #left branch of top node is not yet visisted
                #push right child
                if top[0].right:
                    stack.insert(0, [top[0].right, 0])
                    
                #push back the current node with is_left_visited set to 1
                stack.insert(0, [top[0], 1])
                
                #push left child
                if top[0].left:
                    stack.insert(0, [top[0].left, 0])
            else: #top[1] == 1
                if found:
                    return top[0]
                
                if p.val == top[0].val:
                    found = 1
                
                
        return None 

"""
test
"""
myTest = Solution()
n = TreeNode(1)
myTest.inorderSuccessor(n, n)
