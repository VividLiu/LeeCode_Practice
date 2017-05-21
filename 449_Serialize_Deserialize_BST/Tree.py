#**************************************************************************
#Definition for a binary tree node.
#**************************************************************************
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#**************************************************************************
#Definition for a binary tree
#**************************************************************************
class Tree(object):
    
    _debug = 0 #class variable, which is shared by all class instances.
               #change it from one class instance will lead to change in all other instances

    #**********************************************************************
    #Constructer, build a binary tree using a level order traverse sequence
    #**********************************************************************
    def __init__(self, vals):
        """
        :type vals: List[num]
        :rtype: tree (root tree node)
        """

        #instance variable, bound to specific class instance 
        #tree root node
        self.root = None

        if len(vals) == 0:
            return 
       
        #queue, the nodes in queue are the nodes append to tree but waiting for their child nodes to be appended. If both left and right child nodes have been appended, the node will be removed from queue.
        #initialize the queue with first tree node
        queue = [ TreeNode(vals[0]) ]

        #a pointer to current node whose child nodes are waiting to be appended
        #when both its left child node and right node get appended, update the cur pointer to the next top element in queue
        cur = queue[0] 

        self.root  = cur 

        #a flag to indicate which child, left or right, needs to be appended to cur node
        isLeft = 1 #1, append to left child

        #step by step illustration
        #ex. vals = [3, 2, 4, 1, null, 5, 6]
        #inital queue=[(3)], (n) denotes node with value n
        #   i    new node,  cur,  queue before pop,       tree,    pop
        # i = 1     (2)     (3)   [(3),(2)]                 3
        #                                                  /
        #                                                 2
        #
        # i = 2     (4)     (3)   [(3),(2),(4)]             3      pop(3)
        #                                                  / \
        #                                                 2   4
        #
        # i = 3     (1)     (2)   [(2),(4),(1)]             3
        #                                                  / \
        #                                                 2   4
        #                                                /
        #                                               1
        #
        # i = 4     (null)  (2)   [(2),(4),(1)]             3      pop(2)
        #                                                  / \
        #                                                 2   4
        #                                                /
        #                                               1
        #
        # i = 5     (5)     (4)   [(4),(1),(5)]             3
        #                                                  / \
        #                                                 2   4
        #                                                /   /
        #                                               1   5
        #
        # i = 6     (6)     (4)   [(4),(1),(5),(6)]        3        pop(4)
        #                                                 / \
        #                                                2   4
        #                                               /   / \
        #                                              1   5   6
        for i in xrange(1, len(vals)):
            #construct a tree node using current value
            #append this node to tree, and enqueue this node
            node = None
            if vals[i] != None:
                node = TreeNode(vals[i])
                queue.append(node) #is node is None, no need enqueue

            #debug
            if self._debug:
                print "----------------------------------"
                print "create a new node: " + str(vals[i])


            if isLeft == 1: #append to left child
                #debug
                if self._debug:
                    print "append this new node to left child of " + str(cur.val)
                cur.left = node
                isLeft = 0
            else:
                #debug
                if self._debug:
                    print "append this new node to right child of " + str(cur.val)
                cur.right = node
                isLeft = 1
                #dequeue cur from queue 
                queue.pop(0) 
                #update cur to top elemen in queue
                cur = queue[0]

            #debug
            if self._debug:
                print "current queue:"
                print list(x.val for x in queue)
    
    #**********************************************************************
    #Output the flattened tree structure in level traversal sequence
    #**********************************************************************
    def bfsPrint(self):
        """
        :type t: Tree
        """
        if self.root is None:
            print []

        #return list, level traversal sequence of tree
        rlist = []

        #bfs queue
        queue = [self.root]

        while len(queue) != 0:
            e = queue.pop(0)

            if e is not None:
                rlist.append(e.val) 

                queue.append(e.left) #even if e.left or e.right is None, enqueue
                queue.append(e.right)
            else:
                rlist.append(None)

        print rlist

#---------------------------------------------------------------------
#Output tree structure given TreeNode
#---------------------------------------------------------------------
def bfsNodePrint(rootNode):
    """
    :type t: TreeNoe
    """
    if rootNode is None:
        print []

    #return list, level traversal sequence of tree
    rlist = []

    #bfs queue
    queue = [rootNode]

    while len(queue) != 0:
        e = queue.pop(0)

        if e is not None:
            rlist.append(e.val)

            queue.append(e.left) #even if e.left or e.right is None, enqueue
            queue.append(e.right)
        else:
            rlist.append(None)

    print rlist
"""
test
"""
myTree = Tree([3,2,4,1,None,5,6])
myTree.bfsPrint()

        
        

