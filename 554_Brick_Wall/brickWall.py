"""
Solution:
Get the most frequenct brick space which is not the vertical, then use the number of rows of wall to subtract the frequency.

Ex. 
wall = 
[
 [1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]
]
 
brick space (running sum):
[
 [1, 3, 5, 6]
 [3, 4, 6]
 [1, 4, 6]
 [2, 6]
 [3, 4, 6]
 [1, 4, 5, 6]
]

The most frequent space across rows of walls and is not vertical edge is:
4.
Thus, (number of rows) 6 - 4 (frequency) = 2

"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        num_walls   = len(wall)
        total_width = sum(wall[0])
        
        #calculate running sum (brick space) for each row of wall
        for w in wall:
            for i, br in enumerate(w):
                w[i] += w[i-1] if i > 0 else 0
        
        #use Counter to get the most frequent space which is not the vertical edge
        cnt = collections.Counter(reduce(lambda x, y: x + y, wall, []))
        
        for l, f in cnt.most_common():
            if l != total_width:
                return num_walls - l
            
        return num_walls
