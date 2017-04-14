class Solution(object):
    _debug = 0

    #******************************************************************************
    #******************************************************************************
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #return list
        rlist = []

        if root is None:
            return []

        #call subsumTree function to convert the original tree to subsum tree
        self.subsumTree(root)

        #bfs traverse to get level traversal sequence
        q = [root]
        #list to store level traversal sequence
        l = []

        while len(q) != 0:
            e = q.pop(0)
            l.append(e.val)
                
            if e.left:
                q.append(e.left)
            if e.right:
                q.append(e.right)

        if self._debug:
            print "the level traversal sequence of converted subsum tree is"
            print l

        #use a counter collection to find the most frequenct tree sum
        c = collections.Counter(l).most_common()

        if self._debug:
            print "the result of most_common() function"
            print c

        #the hightest frequence since the result of most_common() is ordered from most common to least common
        mf = c[0][1]

        for tup in c:
            if tup[1] == mf: 
                rlist.append(tup[0])
    
        return rlist 

    #******************************************************************************
    # function subsumTree() 
    # Return the subsum of node t and recursively change every node val to its 
    # subsum, the tree t will be converted to a subsum tree after this function. 
    # Note: subsum is the sum of all the nodes values of its descendents plus 
    # the value of the current node itself.
    #******************************************************************************
    def subsumTree(self, t): 
        """ 
        :type t: TreeNode
        """
        if t is None:
            return 0
            
        subsum = t.val 

        if t.left:
            subsum += self.subsumTree(t.left)
        if t.right:
            subsum += self.subsumTree(t.right)

        #convert the current node val to subsum val
        t.val = subsum

        return subsum

"""
test

myTest = Solution()

#testcase 1
t1 = Tree([5,2,-5])
print "tc1: tree = [5,2,-5]"
print myTest.findFrequentTreeSum(t1.root)
#==> [2]

#testcase 2
t1 = Tree([5,2,-3])
print "tc2: tree = [5,2,-3]"
print myTest.findFrequentTreeSum(t1.root)
#==> [2, -3, 4]

#testcase 3
t1 = Tree([3,2,1,7,None,5,3])
print "tc1: tree = [3,2,1,7,None,5,3]"
print myTest.findFrequentTreeSum(t1.root)
#==> [9]
"""

