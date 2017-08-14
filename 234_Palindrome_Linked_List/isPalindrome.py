# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Solution:
First, think of the possible cases that the linked list can be a palindrome:
1). When the length of the linked list is even.
    ex. [1, 2, 2, 1] when the first half [1,2] = reseved rest half [2,1]
2). When the length of the linked list is odd.
    ex. [1], [1, 2, 3, 2, 1] when the first half separated by the middle pivot is equal to the reversed rest
        [1,2] = [2,1] 

If we need to make sure the time complexity is O(n) and space complexity is O(1),
we can first locate the middle point of the linked list and reverse the latter half linked list,
and use two pointers to traverse the two halfs at the same time and compare its nodes' values.

Note: the way to find the middle point is to use two pointers, 'fast' and 'slow', fast will increment two nodes at each time,
while slow will only increment one node at each time; thus when fast reaches the end of list, slow will stop at middle point.
Ex. [1, 2, 3, 4], 'slow' will stop at elemnt 3
    [1, 2, 3], 'slow' will stop at element 2

After locating the middle point, we can reserve the latter half.
Ex. 1->2->2->1    ==>  1->2->2<-1     
    1->2->3->2->1 ==>  1->2->3<-2<-1, 
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #use two 'fast', 'slow' pointers to locate the middle point
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the latter half list
        pre, cur, nex = None, slow, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
            
        #compare first half and second half
        #remember to distinguish even or odd case
        first, second = head, pre
        while second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
            
        return True
        
