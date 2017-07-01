"""
Question to ask:
1). Are the elements in nums unique? Ex. if nums = [1,2,3,3], then 1st, 2nd larget numbers are both 3, 3?
"""
class Solution(object):
    def findKthLargest(self, nums, k): 
        """
        :type nums: List[int]
        :type k   : int
        :rtype    : int
        """

        if len(nums) == 0 or (k < 1 or k > len(nums)):
            print "error: unapplicable input"  
            return None

        nums.sort(reverse = True)
        return nums[k-1]

"""
Solution: heapsort
Time complexity: O(klogn)
"""
# define my own heapify function which transform a list into max heap in place with array representation
# @param: list[int]
def myHeapify(nums):
    for i in xrange(len(nums)-1, -1, -1):
        heapify_helper(nums, i)

#heapify subtree rooted at i
def heapify_helper(nums, i):
    #the heapify operation has to be bottom-up direction
        lchild, rchild = 2*i + 1, 2*i + 2
        max_idx = i

        #compare with left child
        if lchild < len(nums) and nums[lchild] > nums[max_idx]:
            max_idx = lchild

        #compare with right child
        if rchild < len(nums) and nums[rchild] > nums[max_idx]:
            max_idx = rchild

        if max_idx != i:
            #swap
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

            #after swap, the heap structure of swapped substree might be destroyed
            #thus, need to re-heapify the substree
            heapify_helper(nums, max_idx)

#pop out the largest element in heap
# @param: max heap
# @return param: int
def myHeappop(nums):
    #the largest element in max heap is in top
    largest = nums[0]

    #restore heap structure
    #swap the last element with the first element and reduce the heap size by one
    #restore the heap structure
    nums[0] = nums[-1]

    #trash the last element
    nums.pop()

    myHeapify(nums)

    return largest

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k   : int
        :rtype    : int
        """
        if len(nums) == 0 or (k < 1 or k > len(nums)):
            print "error: unapplicable input"
            return None

        #heapq.heapify() api transform list into a min heap
        #it takes linear time

        #heapq.heapify(nums)
        myHeapify(nums)

        kLargest = 0

        #for i in xrange(len(nums)-k + 1):
        #    kLargest = heapq.heappop(nums)

        for i in xrange(k):
            kLargest = myHeappop(nums)

        return kLargest
  
"""
Solution: quickselect
Time complexity: O(n)
Worst time complexity: O(n^2)
Best time complexity: O(n)
Average time complexity: O(n)
"""
class Solution(object):
    def findKthLargest(self, nums, k): 
        return self.quickSel(nums, 0, len(nums)-1, len(nums)-k)      

    #select kth elemnts in the sorted nums version 
    #nums: list[int] unsorted
    #k   : int, the index of element wanted in sorted array of nums
    def quickSel(self, nums, low, high, k): 
        if k < low and k > high:
            print "error: k is out of nums index"
            return None

        if low <= high:
            pi = self.partition(nums, low, high)

            if pi == k:
                return nums[pi]
            elif k > pi: 
                return self.quickSel(nums, pi+1, high, k)
            elif k < pi: 
                return self.quickSel(nums, low, pi-1, k)
                
    #partition array into two part with a pivot, where nums[0:pi) are all numberssmaller than nums[pi], and nums[pi+1:] are all numbers that are larger than nums[pi]
    #nums[pi] is in the correct position which means nums[pi] is the pi+1 largest element
    def partition(self, nums, low, high):
        #use the last element as pivot
        pivot = nums[high]

        #num[low, s] are all numbers smaller than pivot
        s = low - 1
        for i in xrange(low, high):
            if nums[i] < pivot:
                s += 1
                #swap
                nums[s], nums[i] = nums[i], nums[s]
        nums[s+1], nums[high] = nums[high], nums[s+1]

        return s+1


        
