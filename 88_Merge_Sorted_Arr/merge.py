"""
Time complexity: O(n^2) since it takes O(n) to insert a value in any index in list
"""
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        #two pointer for nums1, nums2 respectively
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums[j]:        
                i += 1
            else: #nums1[i] >= nums2[j]
                nums1.insert(i, nums2[j]) 
                i += 2    
                j += 1

        if j < len(nums2):
            nums1.append(nums2[j])
            j += 1    

"""
Solution:
Since nums1 already has enough space which is m+n+1 length, we can place element from the last one to avoid moving elements backwards while inserting.
Time complexity: O(n) 
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int, length of nums1
        :type nums2: List[int]
        :type n: int, length of nums2
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m+n-1
        while m > 0 and n > 0 and i >= 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1        
    
            i -= 1
            #print "m, n, i: ", m, n, i
            #print "nums1: ", nums1

        if n > 0:
            nums1[:i+1] = nums2[:n]

"""
test
"""
myTest = Solution()
print myTest.merge([1,3,5,-1, -1, -1, -1], 3, [2,4,6,7], 4)
print myTest.merge([3,5,-1,-1,-1,-1], 2, [2,4,6,7], 4)

















