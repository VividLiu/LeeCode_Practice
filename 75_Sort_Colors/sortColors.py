"""
Basically, the question is given an array of n integers which can only be 0, 1 or 2, sort them in ascending order.
Surely we can use generic sorting algorithm like bubble sort which tames O(nlogn) time since it applys to any array. 
However, we don't take some special condition here, which is that the array only contains three possible integers 0, 1, 2, if go with generic sorting algorithm. 
With this condition, we can use some spcecial method to sort the array.
1) Count sort
    Use one-pass to count total numbers of 0s, 1s, 2s separately. Then use 2nd pass to fill the array accordingly.
Time Complexity: O(2n) = O(n)
2) Two pointer, one to indicate the end of already sorted 0 which starts from start of the array and moves forwards; another one to indicate the start position of already sorted 2 which starts from end of the array and moves backwards.
    Keep a cur pointer to iterate through the integer array, if the cur poniter pointing to 0, then swap it with 0s indicator pointer and increment 0s indicator pointer; if the cur pointer pointing to 1, then swap it with 1s indicator pointer and decrement 1s indicator pointer
Time complexity: O(n) one pass
"""
class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        front, back = -1, len(nums)
        
        #locate initial front position which is the first non-zero element
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                front = i
                break
            i += 1
        
        #this array only contains 0s
        if i == len(nums):
            return None
                
        #locate initial back position which is the first non-two element
        i = len(nums) - 1
        while i >= 0:
            if nums[i] != 2:
                back = i
                break
            i -= 1
        
        if i == -1:
            return None
        
        #sort
        i = front
        while front < back and i <= back:
            #swap with front
            if nums[i] == 0:
                nums[i] = nums[front]
                nums[front] = 0
            #swap with back
            elif nums[i] == 2:
                nums[i] = nums[back]
                nums[back] = 2
            else: #nusm[i] == 1                    
                i += 1
                
            #adjust front and back position after swap
            while front < back and nums[front] == 0:
                front += 1
            while front < back and nums[back] == 2:
                back -= 1
            if i < front:
                i = front

"""
The more concise and thorough version of two-pointer solution. It is also Dutch National Flag algorithm.
Keep three pointers: f, b, i
nums[0:f-1] are 0s
nums[f:i-1] are 1s
nums[i:b]   are numbers that haven't been evaluated yet, which are unknow
nums[b+1: ] are 2s

Pseudo:
    while i <= b:
       if nums[i] == 0:
            swap(nums[i], nums[f])
            i++, f++
       if nums[i] == 1:
            i++
       if nums[i] == 2:
            swap(nums[i], nums[h])
            h-- 
            # i doen't increment here, because nums[h] is still unknow, thus after swapping, nums[i] remain unknow.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: list[int]
        """
        f, b, i = 0, len(nums)-1, 0
        
        while i <= b:
            if nums[i] == 0:
                nums[i], nums[f] = nums[f], 0
                f += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], 2
                b -= 1
        
        return None
                


"""
test
"""
myTest = Solution()

#testcase 1:
print "------------------------"
print "nums = [0, 0, 0, 0]"
nums = [0,0,0,0]
myTest.sortColors(nums)
print nums

#testcase 2:
print "------------------------"
print "nums = [1,1,1,1]"
nums = [1, 1, 1, 1]
myTest.sortColors(nums)
print nums

#testcase 3:
print "------------------------"
print "nums = [2,2,2,2]"
nums = [2, 2, 2, 2]
myTest.sortColors(nums)
print nums

#testcase 4:
print "------------------------"
print "nums = [0, 0, 1, 1, 0, 0, 1, 2, 2]"
nums = [0, 0, 1, 1, 0, 0, 1, 2, 2]
myTest.sortColors(nums)
print nums

#testcase 5:
print "------------------------"
print "nums = [1, 2, 0, 0, 1, 1, 0, 0, 1, 2, 2, 0]"
nums = [1, 2, 0, 0, 1, 1, 0, 0, 1, 2, 2, 0]
myTest.sortColors(nums)
print nums

#testcase 6:
print "------------------------"
print "nums = [2,1]"
nums = [2, 1]
myTest.sortColors(nums)
print nums

#testcase 6:
print "------------------------"
print "nums = [1,2,0]"
nums = [1,2,0]
myTest.sortColors(nums)
print nums

#testcase 7:
print "------------------------"
print "nums = [2,1,1,0]"
nums = [2,1,1,0]
myTest.sortColors(nums)
print nums

                
