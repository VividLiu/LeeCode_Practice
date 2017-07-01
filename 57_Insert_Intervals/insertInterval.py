# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


"""
Time complexity: O(n), n the total number of intervals in intervals list
Space complexity: maximally O(n)
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """ 
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        #sanity check
        if newInterval == None:
            return intervals
        if intervals == None or len(intervals) == 0:
            return [newInterval]
        #return list
        res = []

        for i, intv in enumerate(intervals):
            #overlap
            if newInterval.start <= intv.end and newInterval.end >= intv.start:
                #merge newInteval and intv
                newInterval.start = min(newInterval.start, intv.start)
                newInterval.end   = max(newInterval.end, intv.end)
                
                #if this newInterval merge with the last one in interval list
                #add the new one into result now
                if i == len(intervals) - 1:
                    res.append(newInterval)
            elif newInterval.end < intv.start: #no overlapping and newInterval appear in front of intv in list
                res.append(newInterval) 
                
                #put the rest of intervals in list into result
                while i < len(intervals):
                    res.append(intervals[i])
                    i += 1
                break
            elif newInterval.start > intv.end: #no overlapping and newInterval appears later than intv in list
                res.append(intv)
                
                if i == len(intervals) - 1:
                    res.append(newInterval)
            else:   
                print "error: some case I missed considering"
            
        return res
        
"""
test
"""
myTest = Solution()
        
