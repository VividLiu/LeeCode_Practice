"""
Solution:
Get the single pair order first, then represent them using graph. The valid topological order is the rule for the new language.
Ex. ["wrt", "wrf", "er", "ett", "rftt"]
1). From ['wrt', 'wrf', 'er', 'ett', 'rftt'], compare the first letter in each word, we can get the order pairs:
    ('w','e'), ('e', 'r')
2). From ['wrt, 'wrf'], compare the third letter in each words, we can get the order pairs:
    ('t', 'f')
3). From ['er', 'ett'], compare the second letter in each word, we can get the order pairs:
    ('r', 't')
The order pair means, ex ('w', 'e'), 'w' must appear in front of 'e'; thus, we can use topological sort to get the new lexicographical order. 
"""
class Solution(object):
    _debug = 1

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        #List[List[str]], ex. [['w', 'r'], ['r', 'e']]
        #it means 'w' must appear in front of 'r', and 'r' must appear in front of 'e'
        orders = []

        #recursively get orders
        #version 1:
        #self.getOrder(words, 0, len(words), 0, orders, 1)
        #version 2:
        orders = self.getOrder_v2(words)

        if self._debug:
            print "the single pair orders are: ", orders
        #using togological sort to get order
        return self.topoSort(words, orders)

    # use zip() build in function to simplify getOrder() function
    def getOrder_v2(self, words):
        edges = []
        for pair in zip(words, words[1:]):
            for v0, v1 in zip(pair[0], pair[1]):
                if v0 != v1:
                    edges.append([v0, v1])

        return edges    
        
    # recurisvely function to find the single pair order
    # @param words: List[str],  the words list
    # @param start: int,        start position in word list of current search interval
    # @param end  : int,        end position in word list of current search interval
    # @param ind  : int,        index in single word 
    # @param orders:List[List], containers of found order pairs
    def getOrder(self, words, start, end, ind, orders, sp):
        grpStart, grpEnd = start, start
        
        if self._debug:
            print "-" * sp, "search intervals: ", words[start], " -> ", words[end-1], " index: ", ind

        for i in xrange(start, end):
            # use two special characters '/' and '#' to denote two special conditions
            #'/' denotes that ind is out of the current word index
            #'#' denotes that char is already the last character, thus next_char is not valid 
            if len(words[i]) <= ind:
                char = '/'
            else:
                char = words[i][ind]

            if i < end-1: #char is not last word in current search interval
                next_char = words[i+1][ind] if ind < len(words[i+1]) else '/'
            else: #char is last word in current search interval
                next_char = '#'

            grpEnd += 1

            #if char is the character from last word, next_char = '/'
            #it makes sure that char != next_char
            if char != '/' and char != next_char: 
                if next_char != '#':
                    if self._debug:
                        print "-" * sp, "new edge: ("+char+","+next_char+")"
                    orders.append([char, next_char])
                if grpEnd - grpStart > 1: #this group has more than one word
                    self.getOrder(words, grpStart, grpEnd, ind+1, orders, sp+1)
                grpStart = grpEnd
    
    # given an edge list, return the possible topological order
    def topoSort(self, words, edges):
        #get the vertices (which are unqiue characters in words)
        vertices = reduce(lambda x, y: set(x) | set(y), words)

        #transform the edge list to adjacent list
        ad_list = { v: [] for v in vertices}
        for e in edges:
            ad_list[e[0]].append(e[1])

        if self._debug:
            print "the corresponding adjacent list is: ", ad_list

        #visited dictionary to keep track which vertex is visited
        #0: not visited, 1: visited
        visited = { v: 0 for v in vertices}

        #curpath to keep track all vertices in current search path
        #if there are duplicates in curpath, it means a cycle exists, thus, no topological order exists
        curpath = []
        #stack to store the topological order
        stack = []

        valid = True

        for v0 in vertices:
            if not visited[v0]:
                valid &= self.helper(v0, ad_list, curpath+[v0], visited, stack)     

        if self._debug:
            print "the topological order is:"
            print stack[::-1] if valid else ""

        return stack[::-1] if valid else ""

    # recursively visit all children of current vertex v, only until all its children are visited, vertex v can be pushed into the order stack
    # @param v      : vertex
    # @param adList : List[List[str]], adjacent list to reprenst the graph
    # @param curpath: List, to store all vertices in current searching path, in order to detect cycle
    # @param visited: Dictionary, to store visited or not information for each vertex
    # @param stack  : List, to store the final topological order    
    def helper(self, v, adList, curpath, visited, stack):
        #set v vertex as visited
        visited[v] = 1

        res = True

        #recursively explore children of v
        for v1 in adList[v]:
            if v1 in curpath: #a cycle detected
                return False    
            if not visited[v1]:
                res &= self.helper(v1, adList, curpath+[v1], visited, stack)

        #only when all children of v are visited, we can put v in stack
        stack.append(v) 

        return res

"""
test
"""
myTest = Solution()
print "tc1: words=['wrt', 'wrf', 'wrth', 'er', 'ett', 'rftt']"
myTest.alienOrder(['wrt', 'wrth', 'wrf', 'er', 'ett', 'rftt'])           

print "tc2: words=['z', 'x']"
myTest.alienOrder(['z', 'x'])

print "tc3: words=['z', 'x', 'z']"
myTest.alienOrder(['z', 'x', 'z'])

