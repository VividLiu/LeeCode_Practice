#Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Solution:
    Sort the meetings by start time and place them in a timeline. When one meeting starts, 
current room number incraese one; When one meeting ends, reduce the current meeting room by one.
"""
class Solution2(object):
    def minMeetingRooms(self, intervals):
        """ 
        :type intervals: List[Interval]
        :rtype: int
        """

        #array of all start or end time point tuple
        #(t1,t2): t1 is a time (either start or end), t2 is flag to indicate t1 is a start time or end time. Here, 0 indicates end time; 1 indicates start time
        if len(intervals) == 0:
            return 0

        timeline = []

        for intv in intervals:
            timeline.append((intv.start, 1))               
            timeline.append((intv.end, 0))        

        #sort all time point by timeline order, if two time point are same, put end time in front of start time in array, because that meeting must happen in advance
        #ex. intervals = [[0,30],[5,10],[15,20]]
        #ex. timeline = [(0,start), (5,start), (10,end), (15,start), (20,end), (20,end)] 
        timeline.sort(key=lambda tup: (tup[0], tup[1]))  

        room_num = 0
        max_room_num = 0

        for t in timeline:
            if t[1] == 1: #meeting start, add one room to current room number
                room_num += 1
            elif t[1] == 0:#meeting end, subtract one room from current room number
                room_num -= 1
    
            #record the maximum room number alone the timeline
            if room_num > max_room_num:
                max_room_num = room_num 

        return max_room_num
        
"""
Solution 2: 
    Use min heap.
    Each node in the heap represents a room with a time until when the room is occupied
    1). Sort the meeting intervals by start time first.
    2). Iterate through the sorted meetings. For an upcoming meeting, see if there is an existing room in the heap that can be used for this upcoming meeting. The prerequisite for this room is its end time must be samller or equal to the start time of this upcoming meeting. If it exist, we can use this room for the upcoming meeting, just extend the end time of this room to be the end time of this new meeting. 
        Since we use a min heap in which the room with smallest end time will be put at top. We only need to check if the room at top node satisfy this prerequisite.
    3). If the room at top node can not be used for this upcoming meeting, any rooms in the heap can't either. Thus, we need to create a new meeting room and add it to the heap
    
    Time Complexity: O(nlogn), n is for the iteration, logn is the percolation time for mainting the heap invariant at each loop
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0

        #sort the meeting intervals by start time first
        intervals.sort(key=lambda x: (x.start, x.end))

        #initiate the min heap
        heap = [intervals[0].end]    

        for i in xrange(1, len(intervals)):
            topRoomEnd = heap[0]

            #the current meeting use the top room, since it starts after the latest time the room is occupied
            if intervals[i].start >= topRoomEnd:
                #update the room end time
                heapq.heapreplace(heap, intervals[i].end)
            else: #create a new room and add it to heap
                heapq.heappush(heap, intervals[i].end)

        return len(heap)


