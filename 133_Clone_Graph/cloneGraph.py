#definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


"""
To clone the graph, basically we need to traverse each graph node.
The two systemetic way is BFS and DFS.
However the different part of traversing a tree and a graph is that graph can contain loops. Thus, we need to have some mechanic to mark a node is already visited.
Since each label is unqiue in the graph, we can use a hash table with label as key and the node as value to mark if the node is visited or not.
If the node is already visited, then do not clone another one, but use the one already constructed.

Time complexity: O(n), n is the total number of nodes in graph
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
         
        visited = {}
        return self.copyNode(node, visited) 
    
    # clone a node 
    # @param node, a undirected graph node
    # @param visited, a hashtable with node label as key and node as value, if label x is in visited hashtable, it indicate that node x has been already constructed.
    # @return a cloned undirected graph node
    def copyNode(self, node, visited):
        if node == None:
            return None
        
        if node.label in visited:
            print "error: clone an already cloned node: ", node.label
        
        #clone this node
        newNode = UndirectedGraphNode(node.label) 
        #mark it as visited
        visited[newNode.label] = newNode
            
        for x in node.neighbors:
            if x.label in visited:
                newNode.neighbors.append(visited[x.label])
            else:
                newNode.neighbors.append(self.copyNode(x, visited))
                
        return newNode
        

