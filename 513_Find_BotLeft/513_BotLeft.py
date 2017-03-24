#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def enqueue(self,a):
        self.items.append(a)

    def dequeue(self):
        return self.items.pop(0)

    def qsize(self):
        return len(sefl.items)
    

class Solution(object):
    """
    Use bfs to traverse the tree by depth order.
    Store the value when first entering a new depth level. This will be left most value for current depth
    Thus, the last value being stored is the bottom leftmost value.
    """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        #variable initialization
        d = 0      #max depth by now
        l = None   #leftmost child by now
        q = Queue() #create a queue for bfs 

        #enqueue the root node
        tup = (root, 1)
        q.enqueue(tup)

        #imeplement bfs iteratively
        while( not q.isEmpty()):
            #deque the first element
            t = q.dequeue()    

            # the first time entering next depth
            # update new depth variable d
            # and update new leftmost child variable l
            if(t[1] > d): 
                d = t[1]
                l = t[0].val

            #if child node exist, enque
            if(t[0].left):
                tup = (t[0].left, d+1)
                q.enqueue(tup)
            if(t[0].right):
                tup = (t[0].right, d+1)
                q.enqueue(tup)

        return l
