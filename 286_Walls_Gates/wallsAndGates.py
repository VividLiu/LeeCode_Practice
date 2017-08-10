"""
Solution:
DFS rooted at each 0 (or room); and update distance each dfs iteration
(Time limit exceeds)
"""
class Solution2(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
    
        # functoin disFromGate()
        # closure function
        # recursive function to calculate distance from each room to this specific gate using dfs
        # @param ci, cj: int, index of current cell
        
        # Note: the bug of the logic of thie function is using a visited list to keep track of a cell,
        # if a cell is visited or not, and only if it is not visited, we can update its distance.
        # The counter example is:
        # inf, inf, 0
        # int, int, int
        # If the dfs put cell(i, j+1) to prior to (i-1, j) in recursive call order.
        # Then the distance of cell(0,0) will be 4 rather than 2,
        # since the distance of 4 will be (0, 2)->(1,2)->(1,1)->(1,0)->(0,0),
        # rather than (0,2)->(0,1)->(0,0).
        # And visited(0,0) is already set to 1 the first time, so the next time even it is a shorter path, it won't update the cell
        def disFromGate( ci, cj, d, visited):
            #dist = rooms[ci][cj]
            dist = d
            indArr = [(ci-1, cj), (ci+1, cj), (ci, cj-1), (ci, cj+1)]
            
            for i, j in indArr:
                if i >= 0 and i < len(rooms) \
                    and j >= 0 and j < len(rooms[0]) \
                    and rooms[i][j] != 0 \
                    and rooms[i][j] != -1 \
                    and visited[i][j] == 0:
                        if dist + 1 < rooms[i][j]:
                            rooms[i][j] = dist+1
                        visited[i][j] = 1
                        disFromGate(i, j, dist+1, visited)
        
        # functoin disFromGate_v2()
        # closure function
        # recursive function to calculate distance from each room to this specific gate using dfs
        # @param ci, cj: int, the index of previous cell in route
        # Note: to fix the bug of previous version, we use rooms[i][j] > dist+1 as a condiction to 
        # see if we can update the current cell distance or not rather than visited list
        def disFromGate_v2( ci, cj):
            dist = rooms[ci][cj]
            #dist = d
            indArr = [(ci-1, cj), (ci+1, cj), (ci, cj-1), (ci, cj+1)]
            
            for i, j in indArr:
                if i >= 0 and i < len(rooms) \
                    and j >= 0 and j < len(rooms[0]) \
                    and rooms[i][j] > dist+1:
                        rooms[i][j] = dist+1
                        disFromGate_v2(i, j)
                        
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    visited = [[0] * len(rooms[0]) for _ in xrange(len(rooms))]
                    visited[i][j] = 1
                    #disFromGate(i, j, 0, visited)
                    disFromGate_v2(i, j)


"""
Solution:
BFS rooted at each 0 (or room); and update distance each dfs iteration
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        #closure function
        #bfs
        def disFromGate(I, J):
            queue = [(I, J)]
            
            while queue:
                ci, cj = queue.pop(0)
                indArr = [(ci-1, cj), (ci+1, cj), (ci, cj-1), (ci, cj+1)]

                for i, j in indArr:
                    if i >= 0 and i < len(rooms) \
                        and j >= 0 and j < len(rooms[0]) \
                        and rooms[i][j] > rooms[ci][cj] + 1:
                            rooms[i][j] = rooms[ci][cj] + 1
                            queue.append((i, j))
        
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    disFromGate(i, j)
                    
        print rooms
        
                    
"""
test
"""
myTest = Solution()
myTest.wallsAndGates( [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])

myTest.wallsAndGates([[0,2147483647,-1,2147483647,2147483647,-1,-1,0,0,-1,2147483647,2147483647,0,-1,2147483647,2147483647,2147483647,2147483647,0,2147483647,0,-1,-1,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,-1,0,0,-1,0,0,0,2147483647,0,2147483647,-1,-1,0,-1,0,0,0,2147483647],[2147483647,0,-1,2147483647,0,-1,-1,-1,-1,0,0,2147483647,2147483647,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,0,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,0,2147483647,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,2147483647,0,-1,2147483647,-1,-1,-1,0,2147483647]]
)
