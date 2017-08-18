"""
How to determine if a undirected graph is a tree or not:
If the graph satisfies the following two conditions, it is a tree:
1). the graph has no cycle
2). the graph is connected
"""

"""
Solution 1:
Using DFS/BFS to traverse graph represented by adjacent list
Maintain a visited list to keep track which node is already visited.
If a node is not parent of the current node and is in the adjacent list of current node, then a cycle is detected.
If after the dfs traversal, not every node is visted, then the graph is not connected as one.
"""
class Solution1(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        #initiate an adjacent list
        adlist = { v: [] for v in xrange(n)}
        
        #convert edge list to adjacent list
        for v, w in edges:
            #since it is an undirected list, need to add both
            adlist[v] += [w]
            adlist[w] += [v]
        
        print adlist
        
        #version 1: dfs
        #traverse the adjacent list using dfs
        #-------------------------------------------------------
        #visited = [0] * n
        #if self.dfs(-1, 0, adlist, visited) and all(visited):
        #    return True
        #else:
        #    return False
        #-------------------------------------------------------
        #version 2: bfs
        return self.bfs(n, adlist)
        
    # traverse graph represented by adjacent list using dfs
    # @param n      : int, number of nodes 
    # @param adlist : dict, adjacent list
    # @return type  : boolean, true: no cycle detected, false: cycle detected
    def bfs(self, n, adlist):
        #(node, parent): the element in queue is:
        #current node being visiting, and its dirent parent node in the visiting path
        queue = [(0, -1)]
        
        visited = [0]*n
        
        while queue:
            v, p = queue.pop(0)
            
            visited[v] = 1
            
            for w in adlist[v]:
                if w != p and visited[w] == 1:
                    return False
                elif w != p:
                    queue.append((w, v))
        
        return all(visited)
        
        
    # recursive function to traverse graph represented by adjacent list using dfs
    # @param par    : int, direct parent node of the current visiting node
    # @param cur    : int, current node being visited
    # @param adlist : dict, adjacent list
    # @param visited: List[int], visited array
    # @return type  : boolean, true: no cycle detected, false: cycle detected
    def dfs(self, par, cur, adlist, visited):
        #mark current node as visited
        visited[cur] = 1
        
        
        #recursively traverse the adjacent nodes of current node except its direct parent node
        for w in adlist[cur]:
            if w != par and visited[w]: #the adjacent node is not parent node but already visited, means it is a cycle
                return False
            
            if w != par and not self.dfs(cur, w, adlist, visited): #cycle detected in the child node
                return False
        
        return True
                
"""
Solution 2:
Union Find:
If two nodes from edge belong to same set, then the cycle exists
"""
class Solution(object):
    #union find version 1:
    #quick find
    def union1(self, x, y, ids):
        xid = ids[x]
        for i in xrange(len(ids)):
            if ids[i] == xid:
                ids[i] = ids[y]
                
    def find1(self, x, y, ids):
        return ids[x] == ids[y]   
    
    #union find version 2
    #path compressed quick union
    def root(self, x, ids):
        i = x
        while i != ids[i]:
            ids[i] = ids[ids[i]]
            i = ids[i]    
        
        return i
    
    def union2(self, x, y, ids):
        rx = self.root(x, ids)
        ids[rx] = self.root(y, ids)
    
    def find2(self, x, y, ids):
        return self.root(x, ids) == self.root(y, ids)
        
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        #initialize root array
        #initially, each node is only connected with itself
        root = [ i for i in xrange(n)]
        
        #apply union-find process
        for e1, e2 in edges:
            print "edge: (", e1, ",", e2, ")"
            if self.find2(e1, e2, root): #two nodes belong to same set
                return False    
            else:
                print "union this edge"
                self.union2(e1, e2, root)
            print root
                
        print "root"
        print root
        
        #check if there is only one component in the graph:
        #version 1
        #return all( i == root[0] for i in root)
        #version 2
        return all(self.root(i,root) == self.root(0, root) for i in root)



"""
test
"""
myTest = Solution()
print "tc1"
print myTest.validTree(5, [[0,1], [1,2], [2,3], [1,3],[1,4]])
print "tc2"
print myTest.validTree(5, [[0,1], [0,2], [0,3], [1,4]])
