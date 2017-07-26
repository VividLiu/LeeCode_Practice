"""
Solution reference: 
https://discuss.leetcode.com/topic/93708/c-13-lines-with-explanationrint courses

Solution explanation:
First we sort courses by the end date, this way, when we're iterating through the courses, we can switch out any previous course with the current one without worrying about end date.
Next, we iterate through each course, if we have enough days, we'll add it to our priority queue. if we don't have enough days, then we can either ignore this course, or we can use it to replace a longer course we added earlier.

Example:
Courses = [ (6,7), (3,10), (10, 11), (5,15), (4, 16), (5, 16), (2, 19)]
    Action              Taken courses           total time
    insert((6,7))       (6,7)                       6               
    insert((3,1))       (6,7),(3,10)                9
    ignore((10,11)      (6,7),(3,10)                9
    insert((5,15))      (6,7),(3,10),(5,15)         14
    replace((4,16))     (4,16),(3,10),(5,15)        12
    ignore((5,15))      (4,16),(3,10),(5,15)        12
    insert((2,19))      (4,16),(3,10),(5,15)(2,19)  14

"""
import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """

        #sort courses base on end day
        courses.sort(key=lambda x: x[1])

        heap = [] # use a heap to keep track of current taken courses
                  # since heapq is min-heap, we put -courses[0] in queue, so it always pop out the largest duration 
        days = 0

        #iterate through each course
        for dur, end in courses:
            if days + dur <= end: #we have enough days to take the current course
                heapq.heappush(heap, -dur)
                days += dur
            else: # we don't have enough days to take the current course
                largest = -heap[0]
                if largest > dur: 
                    heapq.heapreplace(heap, -dur)
                    days -= largest - dur

        return len(heap)
            
            

                    
"""
test
"""
myTest = Solution()
print myTest.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
print myTest.scheduleCourse([[5,5], [4,6], [2,6]])
print myTest.scheduleCourse( [[5,15], [3,19], [6,7], [2,10], [5,16], [8,14], [10,11], [2,19]])



          
