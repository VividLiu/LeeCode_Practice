#Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Sort the intervals by start time.

the entrire time line:  |---------------------------------------|
(s0-e0):                |---| 
(s1-e1):                        |---| 
(s2-e2):                                |---| 
Then it is very clear that if a person could attend all meetings, the end time of 
each meeting must be smaller than or equal to the start time of its next meeting.
Thus e(j) <= s(j+1) must be true for all the sorted meeting intervals
"""
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
             
        #no meetings
        if len(intervals) == 0:
            return True

        #sort intervals by start time, then by end time if start time is the same
        intervals.sort(key=lambda intv: (intv.start, intv.end)) 

        for i in xrange(1, len(intervals)):
            pre_meeting = intervals[i-1]
            cur_meeting = intervals[i]

            #there is overlapping
            if pre_meeting.end > cur_meeting.start:
                return False 

        return True

        
