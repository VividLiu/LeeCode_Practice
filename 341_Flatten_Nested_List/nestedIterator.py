#"""
#This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        #pointer of current NestedInteger object in current iterating level, 
        #self._pointer = nestedList[0] if len(nestedList) > 0 else None
        
        #stack to keep track of current iterating list reference and index of which elemen of next 
        self._stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        
        curList = self._stack[-1][0]   #current nestesdList being iterated
        curPtr  = self._stack[-1][1]   #ponter of current elemnt in current iterated nestedList
        
        res = curList[curPtr].getInteger()
        
        #advance pointer
        self._stack[-1][1] += 1
        
        return res
        
    def hasNext(self):
        """
        :rtype: bool
        """
        
        while self._stack:
            curList = self._stack[-1][0]   #current nestesdList being iterated
            curPtr  = self._stack[-1][1]   #ponter of current elemnt in current iterated nestedList
            
            if curPtr < len(curList) and not curList[curPtr].isInteger():
                self._stack.append( [curList[curPtr].getList(), 0])
            elif curPtr >= len(curList):
                self._stack.pop()
                if self._stack:
                    self._stack[-1][1] += 1
            elif curList[curPtr].isInteger():
                return True
                
        return False    
            
"""
Trial class:
Given a nested list which each element can be integer or another nested list, 
Flatten the array.
Ex. [1, [2, 3], [4,[5,6]], [[7], [8]]]
==>
[1, 2, 3, 4, 5, 6, 7, 8]
"""
class TrialIter(object):
    def iter(self, nestedList):
        res = []
        
        self.iter_helper(nestedList, res)
        
        return res
    
    def iter_helper(self, nestedList, res):
        if len(nestedList) == 0:
            return
        
        i = 0
        while i < len(nestedList):
            e = nestedList[i]
            if type(e).__name__ == "int":
                res.append(e)
            else: #type(e) == list
                self.iter_helper(e, res)
        
            i += 1
            
        return 

"""
myTest
"""
myTest = TrialIter()
print myTest.iter([[1,1],2,[1,1]])
print myTest.iter([1, [4, [6]], 3])
print myTest.iter([1, [2, 3], [4,[5,6]], [[7], [8]]])
print myTest.iter([[[1,[2,3]]]])
print myTest.iter([[[1,2],3],4])
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
