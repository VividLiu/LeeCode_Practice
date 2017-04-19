"""
Method 1:
Dynamic programming.
Use a two dimentional array sum[n][n] to store the computed result.
sum[i][j]: the sum of subarray nums[i]:nums[j]
sum[i][i] = nums[i]
sum[0][i] = sum[0][i-1] + nums[i] if i >= 1
sum[i][j] = sum[0][j] - sum[0][i] if i != 0
Since i <= j in subarray, only top right half of sum[n][n] need to be filled.
Thus, the time complexity is n + (n-1) + (n-2) + ... + 1 = n(n+1)/2, which is O(n^2)
"""
class Solution_1(object):
    #debuging flag
    _debug = 0

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #size of nums
        l = len(nums)


        #initialize the 
        sums = [ [ 0 for i in xrange(l)] for j in xrange(l) ]

        #fill dp[][] array
        for i in xrange(l):
            for j in xrange(i, l):
                if i == j:
                    sums[i][i] = nums[i]

                elif i == 0:
                    sums[0][j] = sums[0][j-1] + nums[j]

                else: #i!=j, i!= 0
                    sums[i][j] = sums[0][j] - sums[0][i] + nums[i]

        if self._debug:
            print "the computed dp[][] array is: "
            print sums

        #find the maximum size subarray which sums[i][j] == k
        m = 0 #max size
        ni, nj = -1, -1 #the i, j index for max size subarray
        for i in xrange(l):
            for j in xrange(l):
                if sums[i][j] == k and j - i + 1 > m:
                    #find longer one, update m, ni, nj
                    m = j - i + 1
                    ni, nj = i, j

        return m
        
"""
Solution:
Use hash table to reduce time complexity to O(n)

Loop through nums array to preprocess it and convert it to a range sum array sums[n],
in which sums[i] means the sum from nums[0] to nums[i] inclusively.
If sum[j] - sum[i] == k, the sum of subarray (nums[i] : nums[j] ] is equal to k.
Instead of using two 'for' loops to find all pair of (i, j), we can use hash table to store all {sum[j] : j}, so the time complexity can be reduced to O(n).
If (sum[j] - k ) exist in hash table, it means sum[j] - sum[i] == k, thus subarray (num[i]: nums[j] ] is a candidate to the result.
Or if sum[j] == k, it means the subarray [nums[0]: nums[j]] is a candidate.

Ex.
nums = [-2, -1, 2, 1], k=1
the range sum array is: [ -2, -3, -1, 0]
the hash table: -2 -> 0, -3 -> 1, -1 -> 2, 0 -> 3
1) -2 - 1 = -3 exist in hash table, but index of -3 is higer than that of -2 (h[-3] > h[-2], won't build a subarray 
2) -3 - 1 = -4 (X)
3) -1 - 1 = -2 exist, subarray = (0:2] which is [-1, 2]
4)  0 - 1 = -1 exit,  subarray = (2:3] which is [1]
"""
class Solution_2(object):
    #debuging flag
    _debug = 1

    def maxSubArrayLen(self, nums, k): 
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #return result
        m = 0
    
        #hash table
        mp = {}

        #initialize array of sumbarray sum
        sums = [ 0 for x in nums ]

        #convert nums array to array of subarray (nums[0]:nums[i]) sum
        #and create a hashmap for every sum value with sum as key and its index as value
        for i in xrange(len(nums)):
            if i > 0:
                sums[i] = sums[i - 1] + nums[i]
            else:
                sums[0] = nums[0]
    
            #store the (sum, index) into hash table
            #mp[sums[i]] = i #since some subarray sum could be same, we need to store the index into list
            #if sums[i] doesn't exit in mp, create a new list for the key
            #else append it to the existing list
            mp.setdefault(sums[i], []).append(i)

        if self._debug:
            print "array of subarray sum is:"
            print sums
            print "hash table is:"
            print mp

        #find 
        for key in mp: 
            if key == k and max(mp[key]) > m-1:
                m = max(mp[key]) + 1
            else:
                new_key = key - k
                if (new_key in mp) and min(mp[new_key]) < max(mp[key]) and max(mp[key]) - min(mp[new_key]) > m:
                    #sum of subarray nums[ni]:nums[nj] is equal to k
                    #which ni = mp[new_key] + 1, nj = mp[key]
                    m = max(mp[key]) - min(mp[new_key])

        return m

"""
Solution optimization:
The above code can be concised in the following three aspects.
1). No need to create a sums array, just calculate the range sum on the fly when loop through nums array, and store the (sum[i], i) in hash table directly.
2). No need to wait until the hash map is totally established, to test the condition 'if sum[j] - k exist in hash table as sum[i] and i < j' for each j.
    Along the loop while we are building the hash table, we can test the condition for the current (sum[j], j). In that way, if sum[j] - k exist in hash table, denote as sum[i], i must be smaller than j since sum[i] is established before sum[j].
3). No need to use a list to store all indices for a key in hash table when they have same range sum. For example, {sum[i]: [i, i', i"]}, (sum[i] = sum[i'] = sum[i"]). Only need to store the smaller i in hash table because we only need to find the longest subarray. If sum[j] - sum[i] == k, it means subarray nums[i+1]:nums[j], nums[i'+1]:nums[j], nums[i"+1]:nums[j] are all valid candidates, since i is the samllest among (i, i', i"), nums[i+1]:nums[j] is the longest
4). Initialize the hash table with {0:-1} to unify the case of subarray sums: sum[j]-sum[i] and sum[j].
"""
class Solution(object):
    #debuging flag
    _debug = 1

    def maxSubArrayLen(self, nums, k): 
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #hash table
        htable = {0:-1}
        #range sum
        rsum = 0
        #maximum size
        m = 0

        #
        for j in xrange(len(nums)):
            #calculate range sum from 0 to i inclusively
            rsum += nums[j] 
            
            #store the smallest index for that range sum in hash table
            if rsum not in htable:
                htable[rsum] = j

            if rsum - k in htable:
                m = max(m, j - htable[rsum-k])

        return m
                
            
"""
#test
"""   

myTest = Solution()
#testcase 1):
print "tc1: nums=[], k=1"
print myTest.maxSubArrayLen([], 1)
#==> 0

#testcase 2):
print "tc2: nums=[-2,-1,2,1], k=1"
print myTest.maxSubArrayLen([-2, -1, 2, 1], 1)
#==> 2

#testcase 3):
print "tc3: nums=[1,-1,5,-2,3], k=3"
print myTest.maxSubArrayLen([1, -1, 5, -2, 3], 3)
#==> 4

#testcase 4):
#with only one element
print "tc4: nums=[-1], k=-1"
print myTest.maxSubArrayLen([-1], -1)
#==> 1

#testcase 5):
#with some subarray having same sum
print "tc4: nums=[1, 0, -1], k=-1"
print myTest.maxSubArrayLen([1, 0, -1], -1)
#==> 2

#testcase 6):
#with k = 0
