"""
Backtracking:
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        #search the following candidates starting from index start which can sum up to rem
        #param rem   : int, remaining sum
        #param start : int, search starting point
        #param curres: List, current combination
        #param res   : List[List], list of all valid combinations
        def bt(rem, start, curres, res):
            #print "bt: ", rem, start, curres
            #termination
            #accept current branch
            if rem == 0:
                res.append(curres)
                return
            #reject current branch
            if rem < 0:
                return 

            #generating next level
            for i in xrange(start, len(candidates)):
                #next level also start from start, since the same element can be resued in same combination
                bt(rem-candidates[i], i, curres+[candidates[i]], res)    
            return 

        res = []
        bt(target, 0, [], res)

        return res

"""
test
"""
myTest = Solution()
print myTest.combinationSum([2,3,6,7], 7)
