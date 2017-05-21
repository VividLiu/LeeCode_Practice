from Tree import *

#------------------------------------------------------------------------------
#This problem is a specific case to 297.Serialize and Deserialize Tree.
#So the solution for 297 also works here.
#The difference is it is a binary search tree in this problem.
#Thus, we should utilize the information that the tree is a binary search tree
#to either make the serialized string more compact or make the algorithm more effient
#------------------------------------------------------------------------------
class Codec:

    _debug = 0
    #use preorder dfs traverse algorithm to serialize the bfs tree instead of
    #bfs as we used for 297. And another difference is we don't need to record
    #none node in the serialized string.
    #ex.
    #        8
    #      /   \
    #     3     10
    #    / \     \
    #   1   6     14
    #      / \    /
    #     4   7   13
    #will be serialized as 8,3,1,6,4,7,10,14,13
    #Time complexity: O(n), n is the number of nodes in BST
    #Space complexity: O(h), h is the height of BST
    
    #Space Complexity for DFS explanation: The length of longest 
    #path = m. For each node you have to store its siblings so
    #that when you are done visiting all the children and you come 
    #back to a parent node, you can know which sibling to explore
    #next. For m nodes down the path, you will have to store b 
    #(b is the branching factor) nodes extra for each of the m

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #sanity check
        if not root:
            return ""
        
        #serialized list
        res = []
        
        self.dfs_helper_nonrec(root,res)
        
        return ",".join(map(str, res))
    
    #dfs helper using recursive method
    def dfs_helper_rec(self, node, res):
        """
        :type node: TreeNode
        :type res : list
        """
        if node is None:
            return
        
        res.append(node.val)
        
        if node.left:
            self.dfs_helper(node.left,res)
        if node.right:
            self.dfs_helper(node.right,res)
    
    #dfs helper using iterative method with stack
    def dfs_helper_nonrec(self, root, res):
        """
        :type root: TreeNode
        :type res : list
        """
        
        #sanity check
        if not root:
            return []
        
        #initialize dfs stack
        dfs_stk = [root]
        
        while len(dfs_stk):
            top = dfs_stk.pop(0)
            
            res.append(top.val)
            
            if top.right:
                dfs_stk.insert(0, top.right)
            #since the one inserted later will be pop out first,
            #we push in the order of right child first, then left child
            if top.left:
                dfs_stk.insert(0, top.left)
        
        return res
            
        
        
    
    #We don't need to use special character in the serialized string to indicate
    #a none node when the child node is none since from the serialized string 
    #itself, we can know if the current node has a left or right child.
    #It is because of the nature of BST tree, any node in left subtree must be 
    #smaller value, and any node in right substree must be larger value
    #Time complexity: O(n), n is the number of nodes in BST
    #Space complexity: O(h), h is the height of BST
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """        
        
        #sanity check
        if not data:
            return None
        #split data string into list
        dataList = map(int, data.split(","))
        
        #root node
        root = TreeNode(dataList[0])
        
        #initialize stack with root node value 
        stack = [root]
        
        #index of current value of in dataList
        idx = 1
        
        while len(stack) and idx < len(dataList):
            top = stack[0]
                          
            #construct new node
            new = TreeNode(dataList[idx])
             
            if self._debug:
                print "----------------------"
                print "newly constructed node"
                bfsNodePrint(new)
                print "index:" + str(idx)
                print "stack size:" + str(len(stack))
            
            #if current value is smaller than the top elemnt in stack
            #construct new node with this value and append it as left
            #child of current node
            if new.val < top.val:
                #append to left child
                top.left = new
                #push new node to stack
                stack.insert(0, new)
                
                if self._debug:
                    print "append " + str(new.val) + " to left of " + str(top.val)
            #if the current value is larger than the top element in stack
            #construct new node with this value and append it as right child
            #of the first in stack whose val is smaller, but his parent node has
            #a larger value compared to the new node
            else: # dataList[idx] > top.val
                while new.val > top.val:
                    if len(stack) == 1 or new.val < stack[1].val:
                        top.right = new
                        #once both left and right child are constructed,
                        #pop out this node
                        if self._debug:
                            print "pop out " + str(stack[0].val)
                            
                        stack.pop(0)
                        #push new node in stack
                        stack.insert(0,new)
                        
                        if self._debug:
                            print "append " + str(new.val) + " to right of " + str(top.val)
                    else: # dataList[idx] > stack[1].val, thus stack[0] has no right child
                        #pop out this node
                        if self._debug:
                            print "pop out " + str(stack[0].val)
                        stack.pop(0)
                    
                    #update top
                    top = stack[0]
                    
            idx += 1
            if self._debug:
                bfsNodePrint(root)
        return root
                   

"""
myTest
"""
myTree = Tree([8,3,10,1,6,None,14,None,None,4,7,13,None])
myTree.bfsPrint()

myCodec = Codec()
print myCodec.serialize(myTree.root)
bfsNodePrint(myCodec.deserialize(myCodec.serialize(myTree.root)))
