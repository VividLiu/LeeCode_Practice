"""
backtracking which branch will terminate at level k+1

"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def bt(remK, remN, start, curres, res):
            #termination
            if remK == 0:
                #accep
                if remN == 0:
                    res.append(curres)
                    return
                #reject
                else:
                    return

            if remN < 0:
                return

            #generate next level
            for i in xrange(start, 10):
                    bt(remK - 1, remN - i, i+1, curres+[i], res) 

        res = []
        bt(k, n, 1, [], res)
        return res         

"""
test
"""
myTest = Solution()
print myTest.combinationSum3(3, 9)
