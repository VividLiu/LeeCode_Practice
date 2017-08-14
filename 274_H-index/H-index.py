"""
Solution:
Note: One wrong statement of the question is that "If there are several possible values for h, the maximum one is taken as the h-index." since it is no possible to have more than one h value
Sort the array first in descending order.
If for index i, 
if citations[i] >= i+1, it means the papers from index 0:i all have at least i+1 citations since the papers are sorted in citations descending order;
then if i+1 <= citation[i+1], it means all papers from index i+1: n all have at most i+1 citations;
Thus h = i+1
"""
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        #sort the citations array in descending order
        citations.sort(reverse = True)
        
        h = 0
        for i in xrange(0,len(citations)):
            if citations[i] >= i+1 and (i == len(citations)-1 or citations[i+1] <= i+1):
                h = i+1
        
        return h

"""
Solution:
Use bucket sort.
We create a bucket array which have length n (n = len(papers) + 1), and we increase bucket[i] by one if one paper has i citations. If the paper has more than n citation, we increase bucket[n-1], since we can not have h > n.
After creating the bucket, we can iterate the bucket backwards, and calculate the running sum t for each index i, which means totally t papers have at least i citation.

Ex.
citations = [3, 0, 6, 1, 5]

index:       0, 1, 2, 3, 4, 5
buckets   = [1, 1, 0, 1, 0, 2]
running sum from backwards:
          = [5, 4, 3, 3, 2, 2]
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        buckets = [0] * (n+1)
        
        #create buckets
        for i in xrange(n):
            ind = citations[i] if citations[i] <= n else n
            
            buckets[ind] += 1
        
        #calculate running sum
        total = 0
        for i in xrange(n, -1, -1):
            total += buckets[i]
            
            if total >= i:
                return i

        return 0
"""
test
"""
myTest = Solution()
print myTest.hIndex([5,2,1,5,5,5,6,6])
print myTest.hIndex([1, 2, 3, 4])
print myTest.hIndex([1, 0, 4, 5])
print myTest.hIndex([3, 0, 6, 1, 5])
print myTest.hIndex([5, 4])
