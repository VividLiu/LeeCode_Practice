#---------------------------------------------------------------------------
#Uses dfs or bfs to search the grid and mark the visited island 'x'
# to flag it is already visted
#---------------------------------------------------------------------------
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #sanity check
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        #get grid dimenstion
        m, n = len(grid), len(grid[0])
         
        #return results
        numIslands = 0
         
        #convert the string in grid to array, so its cell value can be modified
        tmpGrid = [ list(grid[i]) for i in xrange(len(grid)) ]
        
        
        for i in xrange(m):
            for j in xrange(n):
                if tmpGrid[i][j] == '1':
                    self.dfs_helper(i, j, tmpGrid)
                    numIslands += 1
        
        return numIslands
                    
    
    #start dfs search from grid[i][j]
    def dfs_helper(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        
        #sanity check
        if i < 0 or j < 0 or i >= m or j >= n:
            print "error: out of grid"
            return 
        
        if grid[i][j] == '0' or grid[i][j] == 'x':
            return 0
        else: #grid[i][j] == '1', mark it as visited
            grid[i][j] = 'x'
        
        #north
        if i > 0:
            self.dfs_helper(i-1, j, grid)
        #south
        if i + 1 < m:
            self.dfs_helper(i+1, j, grid)
        #west
        if j > 0:
            self.dfs_helper(i, j-1, grid)
        #east
        if j + 1 < n:
            self.dfs_helper(i, j+1, grid)
#--------------------------------------------------------------------------
#Use Union-Find algorithm
#And implement union-find uses a list of integers
#ex.  
#     1 1 1 1
#     1 0 0 1
#     0 1 0 1
#     1 1 1 1
#1). Flatten the two dimension array into one dimension
#    The formula to map a two dimension index (i, j) to an one diemensition array is: k = 4*i + j
#2). The root for each node is itself initially
#    [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#3). Iterate through the two dimension grid.
#    If grid[i][j] == '1', check its north (i-1, j) and west (i, j-1) neighbors if they exist. Denote k1 = 4*(i-1) + j, k2 + 4*i + (j-1) which is the corresponding index in union-find array
#    Call find(k1, k2) to see if they belong to same sets
#    If they belong to same set:
#        Union( k=4*i+j, root(k1)) # add grid[i][j] to the same set
#    If they don't belong to same set, union these two sets since grid[i][j] serves as a connecting cell
#        Union(root(k1), root(k2)), then Union(k, root(k1))
#
#Time Complexity: 
#Space Comeplexity: O(N), N is total number of cells in grid
#--------------------------------------------------------------------------
class Solution2(object):
    _debug = 0
    
    #find the root of node a
    def root(self, a, uf_arr):
        node = a
        while node != uf_arr[node]:
            node = uf_arr[node]
            
        return node
    
    #find if node a & b belong to same root, in other words, belong to same set 
    def find(self, a, b, uf_arr):
        if self.root(a, uf_arr) == self.root(b, uf_arr):
            return True
        else:
            return False
        
    #union two set
    #set root(b) as parent of root(a)
    def union(self, a, b, uf_arr):
        uf_arr[self.root(a, uf_arr)] = self.root(b, uf_arr) 
        return 0
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #sanity check
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        #
        numIslands = 0
        m , n = len(grid), len(grid[0])
        #initiate union-find list
        uf_list = [ i for i in xrange( m * n )]
        
        #iterate
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                #the mapped index in one dimension array for 
                #north, west neighbour and current respectively
                k1, k2, k= -1, -1, n*i + j
                
                #debug
                if self._debug:
                    print "    ---"
                    print "    i, j: " + str(i) + ", " + str(j)
                
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        k1 = n * (i-1) + j
                    if j > 0 and grid[i][j-1] == '1':
                        k2 = n * i + (j - 1)
                    
                    if k1 != -1 and k2 != -1: #both north and west are islands
                        if self.find(k1, k2, uf_list): #belong to same set
                            #debug
                            if self._debug:
                                print "    k1, k2 belong to same set"
                            
                            self.union(k, k1, uf_list)
                        else: #belong to different set
                            #debug
                            if self._debug:
                                print "    k1, k2 belong to different set"
                            
                            self.union(k1, k2, uf_list)
                            self.union(k, k2, uf_list)
                            #union k1, k2, thus num of disjointed set reduce one
                            numIslands -= 1
                    elif k1 == -1 and k2 == -1:
                        #debug
                        if self._debug:
                            print "    creat a new set"
                        numIslands += 1
                        
                    elif k1 == -1: 
                        #debug
                        if self._debug:
                            print "    only k2 (west) exist"
                            
                        self.union(k, k2, uf_list)
                    elif k2 == -1: 
                        #debug
                        if self._debug:
                            print "    only k1 (north) exist, k1= " + str(k1)
                            
                        self.union(k, k1, uf_list)
                
                #debug
                if self._debug:
                    print "    ", uf_list
                    print "    num of islands: " + str(numIslands)
                        
        return numIslands
        
        
#--------------------------------------------------------------------------
#Use Union-Find concept
#Maintain a list of sets, each set represents a disjointed set by now
#For each grid[i][j] which is '1'
#Check its north and west neighbour which are grid[i-1][j], grid[i][j-1] if they exist
#If grid[i-1][j] and grid[i][j-1] belong to the same set, add grid[i][j] to that set
#If grid[i-1][j] and grid[i][j-1] belong to different sets, union these two sets since grid[i][j] connect them together, then add grid[i][j] to that unioned set
#Time Complexity: 
#for each cell, there are two find operation to see if a, b belong to same set, and maybe union operation.
#find operation will take O(l) l is the number of disajointed sets
#union operation will take O(pq) p, q are the size of to be unioned sets
#Space Complexity: O(mn), m*n is the size of grid
#--------------------------------------------------------------------------
class Solution3(object):
    _debug = 1
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        #return result, number of disajointed set
        res = 0
        
        #sanity check
        if len(grid) == 0 or grid[0] == "":
            return 0
        
        #
        islands = []
        
        #iterate through each cell in the grid. If it is '1', check which sets
        #its north (denote as grid[i-1][j] and west (denote as grid[i][j-1])
        #neighbors belong to. Because the order we iterate, the north and west
        #neighbors of current one must be iterated and put in some set already.
        #Each set represents one disjointed set. 
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if self._debug:
                    print "    ---"
                    print "    i, j: " + str(i) + "," + str(j)
                
                if grid[i][j] == '1':
                    #start a new set with the current one if its north and west neighbour are water
                    if (i == 0 or grid[i-1][j] == '0') and (j == 0 or grid[i][j-1] == '0'):
                        islands.append( {(i,j)} )
                        
                        if self._debug:
                            print "add new set"
                        
                    elif i == 0 or grid[i-1][j] == '0': # grid[i][j-1] == '1
                        #since grid[i][j] is connected with grid[i][j-1]
                        #put (i, j) into the same set with (i, j-1)
                        for s in islands:
                            if (i, j-1) in s:
                                s.add( (i,j) )
                                break
                        
                        if self._debug:
                            print "add (i,j) into same set with (i,j-1)"
                            
                    elif j == 0 or grid[i][j-1] == '0': #grid[i-1][j] == '1'
                        #since grid[i][j] is connected with grid[i-1][j]
                        #put (i, j) into the same set with (i-1, j)
                        for s in islands:
                            if (i-1, j) in s:
                                s.add( (i,j) )
                                break
                                
                        if self._debug:
                            print "add (i,j) into same set with (i-1,j)"
                    else: #both grid[i-1][j] and grid[i][j-1] are islands
                        s1 = set()
                        s2 = set()
                        s1_ind, s2_ind, ind = -1, -1, 1
                        union_flag = False
                        for k in xrange(len(islands)):
                            #if grid[i-1][j] and grid[i][j-1] belong to same set,
                            #then simply add (i,j) to the same set
                            #if they belong to two different sets
                            
                            #then grid[i][j] serves as a connecting point to
                            #connect these two disjointed sets into one,
                            #so merge them into one set
                            if ( (i,j-1) in islands[k] ) and ( (i-1,j) in islands[k]):
                                islands[k].add( (i,j))
                                
                                if self._debug:
                                    print "add (i,j) into same set with (i-1,j) and (i, j-1)"
                            elif ( (i,j-1) in islands[k] ) or ( (i-1,j) in islands[k]):
                                if ind == 1:
                                    s1_ind = k
                                    ind += 1
                                elif ind == 2:
                                    s2_ind = k
                                    ind += 1
                                    union_flag = True
                                    break
                        
                        if union_flag:
                            if self._debug:
                                print "union two sets: index of these two sets are: " + str(s1_ind) + ", " + str(s2_ind)
                            #add grid[i][j] to either one and union two sets
                            s1 = islands[s1_ind]
                            s2 = islands[s2_ind]
                            s1.add((i,j))
                            islands.append(s1 | s2)
                            
                            islands.remove(s1)
                            islands.remove(s2)

                        
                print islands 
        print islands                 
        return len(islands)
                
"""
test
"""
myTest = Solution()

"""
unit test for root, find, union
print myTest.root(1, [0, 1, 2])
print myTest.root(2, [0, 0, 1])
print myTest.find(2, 4, [0, 0, 1, 0, 3]) 
"""

#testcase 1):
print "---------------------------"
print "tc1: grid = [] ==> 0"
print myTest.numIslands([])

#testcase 2):
print "---------------------------"
print "tc2: grid = [''] ==> 0"
print myTest.numIslands([""])

#testcase 3):
print "---------------------------"
print "tc3: grid = ['0'] ==> 0"
print myTest.numIslands(["0"])

#testcase 4):
print "---------------------------"
print "tc4: grid = ['000'] ==> 0"
print myTest.numIslands(["000"])

#testcase 5):
print "---------------------------"
print "tc5: grid = ['0', '0', '0'] ==> 0"
print myTest.numIslands(["0", "0", "0"])

#testcase 6):
print "---------------------------"
print "tc6: grid = ['0', '1', '0'] ==> 1"
print myTest.numIslands(["0", "1", "0"])

#testcase 6):
print "---------------------------"
print "tc6: grid = ['001'] ==> 1"
print myTest.numIslands(["001"])

#testcase 7):
print "---------------------------"
print "tc7: grid = ['11110','11010','11000','00000'] ==> 1"
print myTest.numIslands(['11110','11010','11000','00000'])

#testcase 8):
print "---------------------------"
print "tc8: grid = ['11100','11000','00100','00011'] ==> 3"
print myTest.numIslands(['11100','11000','00100','00011'])

#testcase 9):
print "---------------------------"
print "tc9: grid = ['111', '010', '111'] ==> 1"
print myTest.numIslands(['111', '010', '111'])


#testcase 10):
print "---------------------------"
print "tc10: grid = ['111', '001', '101', '111'] ==> 1"
print myTest.numIslands(['111', '001', '101', '111'])

#testcase 11):
print "---------------------------"
print "tc11: grid = ['1111111', '0000001', '1111101', '1000101', '1010101', '1011101', '1111111'] ==> 1"
print myTest.numIslands(['1111111', '0000001', '1111101', '1000101', '1010101', '1011101', '1111111'])
