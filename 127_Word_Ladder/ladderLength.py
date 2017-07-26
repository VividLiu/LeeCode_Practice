import collections
"""
Solution: BFS (Time limit Exceeded)
For each word, replace each letter every time and see if it exists in wordList, 
if it exists in wordList and not visited before, put it in queue.
Ex. beginWord = hit, endWord = cog
    wordList = [hot, dot, dog, lot, log, det, fog, git, kit, cog, gut] 
    The illustrated bfs tree:
                                        hit
        change 1st char/                    2 |                     3 \ 
        [   git,           kit  ]     [      hot           ]        []
       1/   2|   3\     1/ 2| 3\          1/     2|     3\
(visited)  [gut]    [] (v) []  []  [  dot, lot]  (v)     []
        1/  2|   3\               1/ 2|     3\
      [] (visited) []            (v) [det]   [dog]
                                    1/ 2| 3\   1|                       2\   3\
                                    [] (v) []  [log, fog, cog(found)]   []   (v)
"""
class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        #initialize bfs queue with (beginWord, steps)
        #steps is the number of steps from beginWord to current word
        queue = collections.deque([(beginWord, 1)])

        #a set to record all words that are already visited to avoid circle operation
        visited = {beginWord}

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            #change ith letter in word each iteration
            for i in xrange(len(word)):             
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    #replace ith letter
                    nextWord = word[:i] + c + word[i+1:]  

                    if nextWord not in visited and nextWord in wordList:
                        queue.append((nextWord, step + 1))
                        visited.add(nextWord)

        return 0

"""
Solution:
To optimize and reduce time complexity, we use bidirectional BFS, and instead of adding word to visited set to
avoid repeating circle, we remove the visited word from wordList, so wordList shrink as the search process goes.

Referenece for bidirectional BFS:
http://www.geeksforgeeks.org/bidirectional-search/

Time comlexity about bidirectional search:
If the distance from source to target is d, and the branching factor is b (every vertex has on verage b edges)
    - BFS will traverse 1 + b + b^2 + b^3 ... b^d vertices
    - bidirectional search will traverse 2 + 2b + 2b^2 + ... + 2b^(d/2) vertices
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        #edge case:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        front, back = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        path = 1

        while front and back:

            #generate next level of candidates of words in front
            #front = { word[:i] + c + word[i+1:] for word in front for i in xrange(len(word)) for c in 'abcdefghijklmnopqrstuvwxyz'}
            nextLevel = set()
            for word in front:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        #found the shortest path when there is intersect vertex in front and back
                        if newWord in back:
                            return path + 1

                        if newWord in wordList and newWord not in visited:
                            nextLevel.add(newWord)
            front = nextLevel

            #add the new generated words into visited set
            visited |= front 

            #increment path 
            path += 1

            #keep front always the shorter list to reduce branching
            if len(front) > len(back):
                #swap
                front, back = back, front    

        return 0

"""
test
"""
myTest = Solution()
print myTest.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print myTest.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])







