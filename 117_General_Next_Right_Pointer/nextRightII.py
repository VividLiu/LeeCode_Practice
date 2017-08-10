"""
Ex.    1
    /    \
   2  ->  3
  / \      \
 4->5 ->    7
 
Ex.    1 -> None
    /    \
   2  ->  3 -> None
  / \    / 
 4->5 -> 7  -> None

Ex. 
        1
      /   \
     2     3
    / \     \
   4   5     6
  /           \
 7             8

The difference that 117 has from 116 is that the tree is not guaranteered to be perfect.
Consider the few above examples, we can not use dfs as we used in 116 to solve this problem. We need to use bfs instead.
Maintain three variables:
parNode : current parent node whose children are being investigated
head    : head of the children level
curNode : curNode in chldren level whose next pointer is to be assigned

"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #initialize variables
        parNode = root
        curNode = TreeLinkNode(0) #create a dummy Node for initial head
        head    = None
        
        while parNode: #iterating different levels
            while parNode: #iterating current level
                if parNode.left:
                    if not head:
                        head = parNode.left
                    curNode.next = parNode.left
                    curNode = parNode.left
                if parNode.right:
                    if not head:
                        head = parNode.right
                    curNode.next = parNode.right
                    curNode = parNode.right
                    
                parNode = parNode.next
            
            parNode = head
            curNode = TreeLinkNode(0)
            head    = None
                
