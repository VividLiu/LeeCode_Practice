"""
The input is an edge list representation for directed graph.
As long as no cycle exist in the graph, it is possible to finish all courses.

Reference: graph representation
1).Edge list
    Space complexity: O(|E|)
    The time complexity to find a specific edge: O(|E|)
2).Adjacent matrics:
    Space complexity: O(|V|^2)
    The time complexity to find a specific edge: O(1)
    The time complexity to find the adjacent vertices: O(|V|)
3).Adjacent list:
    Space complexity: O(|E|)
    The time complexity to find a specific edge: O(d), degree of vertex, 0<=d<=v-1
    The time complexity to find the adjacent vertices: O(1)

Solution:
Topological sorting via DFS (Time Limit Exceeds)
The time complexity for topological soring using edge list data structure is:
O(|E||V|)
To reduce time complexity, preprocess the graph to get an adjacent list, 
the time complexity using an adjacent list is:
O(d|V|), d is the average vertex degree
"""
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        visited = [0] * numCourses
        order = []

        #preprocess graph to adjacent list
        adlist = {}
        for v in xrange(numCourses):
            adlist[v] = []
        for edge in prerequisites:
            adlist[edge[0]].append(edge[1])

        isAcyclic = False

        for i in xrange(numCourses):
            if visited[i] == 0:#not visited yet
                #version 1
                #get topological order
                #self.rec_topoSort(i, visited, order, numCourses, prerequisites)

                #version 2
                #detect cycle using edge list via DFS
                #isAcyclic |= self.isAcyclic(i, visited, [i], numCourses, prerequisites)

                #version 3
                #detect cycle using adjacent list via DFS
                isAcyclic |= self.isAcyclic_adj(i, visited, [i], adlist)

        #return order
        return not isAcyclic
        

    # recursively traverse all vertices which are adjacent to v to get the topological order of the graph
    # @param v      : vertex
    # @param visited: List[int], to mask if vi is visited
    # @param order  : List[int], array of vertices in topological order
    def rec_topoSort(self, v, visited, order, vNum, edges):
        visited[v] = 1

        for i in xrange(vNum):
            if [v, i] in edges and visited[i] == 0: #if i is adjacent to v and i is not visited yet
                self.rec_topoSort(i, visited, order, vNum, edges)          

        order.append(v)

    # recursively traverse all vertices which are adjacent to v in topological order
    # the difference between rec_topoSort and isAcyclic is that isAcyclic function keep track all the verticesin current traverling path. If there are duplicate vertex in current path, it means a cycle exists. 
    # @param v      : vertex
    # @param visited: List[int], to mask if vi is visited
    # @param order  : List[int], array of vertices in topological order
    def isAcyclic(self, v, visited, curPath, vNum, edges):
        visited[v] = 1
        
        res = False

        for i in xrange(vNum):
            if [v, i] in edges and i in curPath: #detect an acyclic
                return True
            if [v, i] in edges and visited[i] == 0: #if i is adjacent to v and i is not visited yet
                res |= self.isAcyclic(i, visited, curPath + [i], vNum, edges)
        
        return res

    # recursively traverse all vertices which are adjacent to v in topological order with adjacent list as graph representation
    def isAcyclic_adj(self, v, visited, curPath, adj_list):
        visited[v] = 1
        
        res = False

        for i in adj_list[v]:
            if i in curPath: #detect an acyclic
                return True
            if visited[i] == 0: #if i is adjacent to v and i is not visited yet
                res |= self.isAcyclic_adj(i, visited, curPath + [i], adj_list)
        
        return res
    
"""
Solution:
Topological sorting via BFS
reference: www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #preprocess graph to adjacent list
        adlist = {}
        for v in xrange(numCourses):
            adlist[v] = []
        for edge in prerequisites:
            adlist[edge[0]].append(edge[1])

        #for each vertex, caculate its in degree
        in_degree = [0] * numCourses
        for edge in prerequisites:
            in_degree[edge[1]] += 1

        #queue that contains all vertices which has no in edge
        #when a vertex has no in edge any more, it means it doesn't have pre requisie any more
        queue = []
        for v, d in enumerate(in_degree):
            if d == 0:
                queue.append(v)

        #decrease the in degree of a vertex's adjacent vertices when it is removed 
        while queue:     
            v_int = queue.pop(0)        
            for v_out in adlist[v_int]: 
                in_degree[v_out] -= 1
                if in_degree[v_out] == 0:
                    queue.append(v_out)
             
        return True if all( in_degree[i] == 0 for i in xrange(numCourses)) else False

"""
test
"""
myTest = Solution()
print myTest.canFinish(6, [[5,2], [5,0], [4,0], [4,1], [2,3], [3,1]])
print myTest.canFinish(6, [[5,2], [5,0], [4,0], [4,1], [2,3], [3,1], [1,5]])
print myTest.canFinish(2, [[0,1], [1,0]])




            
