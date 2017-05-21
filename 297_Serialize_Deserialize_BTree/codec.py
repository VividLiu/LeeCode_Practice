from Tree import *

class Codec:

    #use bfs to serialize tree
    #Time complexity: O(n), n is the number of nodes in Tree
    #Space complexity: O(w), w is the maximum width of the Tree

    #Space complexity for general Tree BFS using queue is:  
    #Extra Space required for Level Order Traversal is O(w) where w is maximum width of Binary Tree. 
    #In level order traversal, queue one by one stores nodes of different level.
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #serialized result in list
        res = []
        
        #sanity check
        if not root:
            return ""
        
        #initialize bfs queue
        bfs_q = [root]
        
        while len(bfs_q) != 0:
            node = bfs_q.pop(0)
            
            #if current node is None, put the children(including None child) of current node into bfs queue
            if node is not None:
                bfs_q.append(node.left)
                bfs_q.append(node.right)
            
            #put current node value into serialiezed result
            #if the current node is None, use special character '/' to replace it
            #res += str(node.val) if node is not None else '/'
            res.append(str(node.val) if node is not None else '/')
        
        return ",".join(res)
    
    
    #the difficulty of deserializing a string back to tree structure is to 
    #keep track of which node needs to be constructed next
    #Use a bfs queue for this purpose, and the nodes in queue are the nodes whose children are needed to be constructed
    #Thus, when enqueue a TreeNode, the value of the node is constructed 
    #if it is a none node, no need to enqueue since no need to construct its children
    #when pop out a TreeNode from queue, construct its children nodes
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        #sanity check
        if len(data) == 0:
            return None
        
        #split the joined data string into list
        dataList = data.split(",")
        
        #index of current node value in serialized string
        #starting from one, since root node is constructed
        idx = 1
        
        #initialize a bfs queue
        root = TreeNode(int(dataList[0]))
        bfs_q = [root]
        
        while len(bfs_q) > 0:
            cur = bfs_q.pop(0)
            
            #construct left child if it is not none and enqueue
            if dataList[idx] != '/':
                left = TreeNode(int(dataList[idx]))
                cur.left = left
                bfs_q.append(left)
                
            idx += 1
            
            #construct right child if it is not none and enqueue
            if dataList[idx] != '/':
                right = TreeNode(int(dataList[idx]))
                cur.right = right
                bfs_q.append(right)
            
            idx += 1
        
        return root
    #Use a bfs queue to keep track of the nodes which are needed to be constructed
    #Thus, initialize a TreeNode instanse holder when put in queue, 
    #when pop out, update the TreeNode value or set it as None if is a None node
    #I think this solution will work using C/C++. 
    #In C/C++, if curNode is pointer pointing to a class instance
    #when we assigne curNode = None, the pointer (or reference location) won't change, the value inside the memory location the pointer is pointing to changes. Thus, the curNode will be None.
    #However, in Python, when we do curNode = None, the reference of curNode is changed to hex(id(None)) which is the memory location of value 'None'. The class instance itself is not changed. It is the reason that this algorithm doesn't work.
   # def deserialize2(self, data):
   #     """
   #     Decodes your encoded data to tree.
   #     
   #     :type data: str
   #     :rtype: TreeNode
   #     """
   #     #sanity check
   #     if len(data) == 0:
   #         return None
   #     
   #     #use a bfs queue to keep track of the nodes that need to be constructed
   #     root = TreeNode(0)
   #     bfs_q = [root]
   #     
   #     #index of current value in serialized string 
   #     idx = 0
   #     
   #     while len(bfs_q) != 0:
   #         e = bfs_q.pop(0)
   #         #not a none node
   #         if data[idx] != '/': 
   #             e.val = int(data[idx])
   #             
   #             #put its children in queue to be constructed
   #             left_child  = TreeNode(0)
   #             right_child = TreeNode(0)
   #              
   #             e.left = left_child
   #             e.right = right_child
   #             
   #             bfs_q.append(e.left)
   #             bfs_q.append(e.right)
   #         else:# a none node
   #             e = None
   #         
   #         print "--------"
   #         print data[idx]
   #         bfsNodePrint(e)
   #         bfsNodePrint(root)
   #             
   #         idx += 1
   #             
   #     return root
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

"""
test
"""
myTree = Tree([3,2,4,1,None,5,6])
myTree.bfsPrint()

myCodec = Codec()
print myCodec.serialize(myTree.root)
bfsNodePrint(myCodec.deserialize(myCodec.serialize(myTree.root)))
