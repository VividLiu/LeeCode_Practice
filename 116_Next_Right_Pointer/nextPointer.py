"""
Ex.    1
    /    \
   2  ->  3
  / \    / \
 4->5 ->6 ->7

From the example above, we can see, there are two types of 'next' pointer;
left  child -> right child, ex, 2->3 or 4->5
right child -> left child,  ex, 5->6
Thus, we need to know how to set the 'next' pointer when it is either a left child or right child
"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        if root.left:
            #since it is a perfect binary tree, the right child always exist
            root.left.next = root.right
            self.connect(root.left)
        
        if root.right:
            root.right.next = root.next.left if root.next else None
            self.connect(root.right)
