"""
Question to ask:
Will p or q always exist in tree?
Can p and q be the same node?
Are the node values in tree unqiue?

Solution: (Time limit exceeds)
If node x is the lowest common ancestor of node p and q. 
Then,
1). x = p or q, then the other one is in subtree of root x, or at the root, if p == q
2). p and q are separately in the left and right subtree of x. They won't appear in the same side of substree of root x.
Thus, we can traverse the treenodes. 
If p and q are located in different sides of current root x, x is the lowest common ancestor. 
If p and q are located in same side, let's say left side, then recursively start the same searching step using the left child of current root as root
If the current root x is one of q or p (or they are same), then x is the lowest common ancestor

Time complexity: O(n^2)
the worst case is that p and q are located in the lowest level.
Ex.  1
    / \
   2   3
  / \
 p   q
Then the time complexity is: O(n) + O(n) (left substree size) + O(n) (left subtree size) ... = O(n^2)
"""
class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        #sanity check:
        if root == None or p == None or q == None:
            return None
        
        #special case
        if (root == p or root == q) and (findNodes(root.left, p, q) or findNodes(root.right, p, q)):
            return root
         
        if findNodes(root.left, p, q) and findNodes(root.right, p, q):
            return root
        
        if findNodes(root.left, p, q) and not findNodes(root.right, p, q):
            return self.lowestCommonAncestor(root.left, p, q)
        
        if findNodes(root.right, p, q) and not findNodes(root.left, p, q):
            return self.lowestCommonAncestor(root.right, p, q)
            
    
    # search if node x or y are in Tree rooted at root
    # @param root  : TreeNode, the root of tree to be searched in
    # @param x, y  : TreeNode, the nodes to search for
    # @return param: int, 1: found; 0: not found
    def findNodes(self, root, x, y): 
        #sanity check:
        if root == None or x == None:
            return 0
        
        stack = [root]
        
        while stack:
            #pop out the top node in stack
            top = stack.pop()
            
            if top == x or top == y:
                return 1
            
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
                
        return 0

"""
Solution: (Memory limit exceeds)

While travsersing the tree using DFS, store each node's path from root to it in an array.
Find the earlest common node in path of p and q.
"""
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        tmp1, tmp2, pPath, qPath = [], [], [], []
        
        if self.findPath(root, p, tmp1, pPath) and self.findPath(root, q, tmp2, qPath):
            for x in pPath[::-1]:
                if x in qPath:
                    return x
        
        
        return None
        
    
    # search path from node to x, if found, return it in foundPath parameter
    # @param node: TreeNode
    # @param x   : TreeNode 
    # @param path: List[TreeNode], store each node in the path from node to to current node
    # @param foundPath: List[TreeNode], store each node in the path from node to to x if x is found, otherwise []
    # @return param: int, 1 found, 0 not found
    def findPath(self, node, x, path, foundPath):
        if node == None:
            return 0
        
        #put current node in path
        path.append(node)
        
        #termination
        if node.val== x:
            for p in path:
                foundPath.append(p)
            return 1
        else:
            return self.findPath(node.left, x, path[:], foundPath) | self.findPath(node.right, x, path[:], foundPath)
            
            
"""
Solution: 
Build a parents hashmap for each node when traversing the tree.
Then we can rebuild the path from node to p and q using the parents hashmap, thus find the lowest common ancestor

Time complexity: O(n + h + h^2)
O(n) for traversing the tree; O(h) for rebuild the path from root q, h is the maximum height of the tree, h <= n; O(h^2) for traversing back grom q to root and check for q's each parent, if it exist in pPath.

Space complexity: O(n)
n for quue, n for parents, n for pPath maximally.
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #sanitcy check
        if root == None or p == None or q == None:
            return None
        
        #traverse the tree using iterative bfs and build parents map with key=node, value = parent node of node, -1 if no parent exists
        queue = [root]
        parents = { root: -1}
        
        while queue:
            top = queue.pop(0)
             
            if top.left:
                parents[top.left] = top
                queue.append(top.left)
                
            if top.right:
                parents[top.right] = top
                queue.append(top.right)
        
        #rebuild path from root to node p and q
        pPath = []
        cur = p
        while cur in parents:
            pPath.append(cur)
            cur = parents[cur]
        
        #while traversing back from q to root, check if the parent exist in pPath
        cur = q 
        while cur in parents:
            if cur in pPath:
                return cur
            cur = parents[cur]
            
            
        return None
        
        
            
"""
test
"""
            

