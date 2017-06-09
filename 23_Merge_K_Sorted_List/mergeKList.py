import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def printListNode(node):
    if not node:
        print "node: None"
    else:
        print "node: ", node.val,

def printList(fNode):
    if not fNode:
        print "List: None"
        return None
    
    p = fNode
    print "List: ",
    while p:
        print p.val,

"""
Keep k pointers pointing at current nodes to be compared in each linked list. And maintain a min heap to get the smallest in these current k element.
Time complexity: O(nlogk), k is length of lists, n is total node number in all linked list
"""
class Solution(object):
    _debug = 0
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        #sanity check
        if len(lists) == 0:
            return None
        
        n = len(lists)
        
        #initialize a min heap, with a three value tuple
        #(val, node, ind)
        #val: the node value, since python heapq will compare using the first element if the heap element is a tuple
        #node: the node with this value
        #ind: the index of the linked list with this node in lists array
        minHeap = []
        for i in xrange(n):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, lists[i], i))
            
        #pointers of current node in heap for each linked list 
        pointers = [ first_node for first_node in lists]
        
        if self._debug:
            print "initial min heap:", minHeap
            print "initial pointers:", [printListNode(nd) for nd in pointers]
        
        #resturn merged list
        res = None
        cur = None
            
        #merge the k sorted list by pop one smallest number in heap, and append that element in returned linked list
        #If the smallest element is in ith linked list, advance the index of ith linked list by one and push that element in heap
        while any(pointers[i] != None for i in xrange(n)): #not reaching end of all linked lists
            if self._debug:
                print "------------------"
            if minHeap:
                smallest = heapq.heappop(minHeap)
                if self._debug:
                    print "     pop out smallest in heap: ", smallest[0]
            else:
                print "error: index out of range in heap"
                
            #add the smallest element in heap to result linked list
            if not res: #append the first node
                cur = smallest[1]
                res = cur
            else:
                cur.next = smallest[1]
                cur = cur.next
            
            if self._debug:
                print "     Add ", smallest[0], " into to final list "
                
            #push the next node of cur to heap if it exists
            nextNode = smallest[1].next
            if nextNode: #nextNode != None
                heapq.heappush(minHeap, (nextNode.val, nextNode, smallest[2]))
                pointers[smallest[2]] = nextNode
                
                if self._debug:
                    print "     Add next node ", printListNode(nextNode), " in heap"
                    print "     current heap:", minHeap
                    print "     current pointers: ", [printListNode(nd) for nd in pointers]
            else:
                
                pointers[smallest[2]] = nextNode
                if self._debug:
                    print "     next node is none"
                
        return res
                
                

"""
test
"""
myTest = Solution()
                
            
            
        
        
        
         
        
        
        
        

