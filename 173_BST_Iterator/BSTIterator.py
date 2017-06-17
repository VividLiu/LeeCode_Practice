#Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
This question is similar to 341.Flatten list iterator which use a stack to keep track of current iterating level.
Similarly, we use a stack to keep track of nodes to be visited in dfs order, thus it will be visited in ascending order since it is a BST.
Element in stack is [node, flag]
node: current node root
flag: 0 means the left branch of current node has not been pushed into stack and visited yet. 1 means the the left branch of current node is already visited.
In the hasNext() function, if the top element in stack has 0 flag, we recursively pushing the left child into stack until the leaf node which will be the next smallest element. If the top element in stack has 1 flag, the current root is the next smallest elemnt. When we pop out one node from stack in next() function, push its right child into stack with 0 flag. (in-order traverse)
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #stack variable to keep track of to be visited nodes in dfs order
        #element in stack is [node, flag]
        #node: current node root
        #flag: 0 means the left branch of current node has not been pushed into stack and visited yet. 1 means the the left branch of current node is already visited.
        self._stack = [[root, 0]] if root != None else []     

    def hasNext(self):
        """
        :rtype: bool
        """
        
        while self._stack:
            top = self._stack[-1]
            #the left branch of top[0] node is already visited, thus the next smallest node will be the current root, which is top[0]
            if top[1] == 1:
                break
            
            #the left branch hasn't visited, keep push the left child until leaf
            if top[1] == 0:
                #set the left branch visited flag to one
                self._stack[-1][1] = 1
                
                #append the left child if it exist
                if top[0].left:
                    self._stack.append([top[0].left, 0])
        
        #return True if stack is not empty
        return not (self._stack == [])
        

    def next(self):
        """
        :rtype: int
        """
        cur = self._stack.pop()
        
        #push the right child of current one to stack since the next smallest element will be the left most child in the right branch of curent root
        if cur[0].right:
            self._stack.append([cur[0].right, 0])
            
        return cur[0].val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

