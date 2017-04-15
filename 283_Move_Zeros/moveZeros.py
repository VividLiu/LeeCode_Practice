#**********************************************************************************
#Method 1):
#Use the same concept of bubble sorting. The difference is instead of swapping when a > b,
# swap when a = 0 
# the time complexity will be O(n^2)
#**********************************************************************************
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in xrange(len(nums)):
            # for the range of j
            # -i: the last i elements are already in place
            # -1: ensure b = nums[j+1] not exceeding index boundary
            for j in xrange(len(nums) - i - 1): 
                a, b = nums[j], nums[j+1] 
    
                #swap a and b if a is 0
                if a == 0:
                    tmp = b 
                    nums[j+1] = a 
                    nums[j] = tmp 


#**********************************************************************************
#Method 2):
#Use two pointer to denote the start (s) and end (e) position of concatenated 0s strings
#Loop through the array, when the current num, num[i] is not 0, swap num[i] with num[s]:nums[e],
#thus, the 0s will be shifted towards the tail of the array. when num[i] is 0, append nums[i]
#to nums[s]:nums[e] to incude nums[i] in the concatenated 0s string.
#**********************************************************************************
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        #the pointer to mark the start and end of the concatenated 0s 
        s, e = -1, -1

        #step by step illustration
        #ex. [4, 0, 1, 0, 3, 12]
        # initial s, e = -1, -1
        # i,  nums[i],  action,     s,   e,       nums
        # 0,    4       none        -1   -1    [4,0,1,0,3,12]         
        # 1,    0       s=e=i        1    1    [4,0,1,0,3,12]         
        # 2,    1       swap         2    2    [4,1,0,0,3,12]         
        # 3,    0       concatenate  2    3    [4,1,0,0,3,12]         
        # 4,    3       swap         3    4    [4,1,3,0,0,12]         
        # 5,    12      swap         4    5    [4,1,3,12,0,0]         
        for i in xrange(len(nums)):
            if nums[i] != 0 and s != -1:#swap 0s and current number if current number is not 0        
                #since from s to e, the elements are all 0
                #only need to swap nums[s] and nums[i]
                nums[s] = nums[i]
                nums[i] = 0
                #update s, e
                s, e = s+1, e+1
            elif nums[i] == 0: #update s and e to include this 0
                if s == -1: #the first time to encounter 0
                    s = e = i
                else: #concatenate the current 0 to (s,e)
                    e += 1
                
#**********************************************************************************
#Solution
#Two pointers, one pointer to record the position which next nonzero element needs
#to be swapped, one pointer to loop through the array.
#When 
#**********************************************************************************
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #the pointer to record the position that next nonzero element needs to 
        #be swapped
        p = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                #swap
                nums[p], nums[i] = nums[i], nums[p]
                #advance p
                p += 1
             

"""
test
"""

myTest = Solution2()

#testcase 1): 
n1 = [0,1,0,3,12]
print "-----------------"
print "tc1: [0,1,0,3,12]"
myTest.moveZeroes(n1)
print n1
#===> [1, 3, 12, 0, 0]

#testcase 2): 
n1 = []
print "-----------------"
print "tc2: []"
myTest.moveZeroes(n1)
print n1
#===> []
    
    
#testcase 3): 
n1 = [0, 0, 0]
print "-----------------"
print "tc3: [0, 0, 0]"
myTest.moveZeroes(n1)
print n1
#===> [0, 0, 0]
    
#testcase 3): 
n1 = [12, 3, 0]
print "-----------------"
print "tc4: [12, 3, 0]"
myTest.moveZeroes(n1)
print n1
#===> [12, 3, 0]

#testcase 4): 
n1 = [12, 0, 0, 3]
print "-----------------"
print "tc5: [12, 0, 0, 3]"
myTest.moveZeroes(n1)
print n1
#===> [12, 3, 0, 0]
        
