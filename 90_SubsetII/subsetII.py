"""
Solution: backtracking
This problem is similar to 78.subsets. 
The difference is duplicates are allowed in nums which might cause redundant subsets when we generate all possible subsets using backtracking algoritm.
Thus, when we generate a new subset we need to check if the subset is already in the final result set.
"""
class Solution2(object):
    def subsetsWithDup(self, nums):
        """ 
        :type nums : List[int]
        :rtype     : List[List[int]]
        """

        #sort nums in place
        nums.sort()
        
        res = [[]]

        for i, e in enumerate(nums):
            newsub = []
            for subset in res:
                if subset + [e] not in res:
                    newsub.append(subset+[e])
            res.extend(newsub)
            
        return res 

"""
Optimaztion for previous solution.
Still use backtracking algorithm. However, instead of checking if the new subset is already in final result list, we avoid generating the duplicated subsets.
How can we avoid generating the duplicated subsets?
ex. nums = [1, 4, 4, 4]
Simulate the generated res in steps:
1). res = [[]]
2). res = [[], [1]]
3). res = [[], [1], [4], [1,4]]
4), res = [[], [1], [4], [1,4], [4,4], [1,4,4]]
    Here, we encountered a duplicate number 4 in nums. thus, if we still add 4 in [[], [1]], it creates duplicated subsets. So we only add 4 in [[4], [1,4]]
5). res = [[], [1], [4], [1,4], [4,4], [1,4,4], [4,4,4], [1,4,4,4]]
    Here, we encountered a second duplicate number 4 in nums. thus, if we still add 4 in [[], [1], [4], [1,4]], it creates duplicated subsets. So we only add 4 in [[4,4], [1,4,4]]
Thus, if we encounter a duplicate number, we only add it to the subsets created by previous step avoid generating duplicates
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums : List[int]
        :rtype     : List[Llist[int]]
        """
        #sort nums in place
        nums.sort()

        #return result
        res = [[]]

        preAdd = 0

        for i, e in enumerate(nums):
            newsub = []

            start = 0
            #encounter duplicate numbers
            if i > 0 and e == nums[i-1]:
                start = len(res) - preAdd

            cnt = 0
            for subset in res[start:]:
                newsub.append(subset + [e])
                cnt += 1

            preAdd = cnt

            res.extend(newsub)

        return res


        
        
