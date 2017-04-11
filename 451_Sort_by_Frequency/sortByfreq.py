import itertools
import collections

"""
Utilize python 'groupby' function
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""

        rlist = []
        
        #step by step illustration using 
        # s = "baby"
        # The output of itertools.groupby(sorted(s)) is:
        # 1), k = a, g = (a)
        # 2). k = b, g = (b, b)
        # 3). k = y, g = (y) 
        for k, g in itertools.groupby(sorted(s)):
            # join the list(g) to a string string and append to rlist
            # iteration 1). rlist.append(['a'])  => rlist = ['a'] 
            # iteration 2). rlist.append(['bb']) => rlist = ['a', 'bb'] 
            # iteration 3). rlist.append(['y'])  => rlist = ['a', 'bb', 'y'] 
            rlist.append( "".join(list(g)))

        #sort rlist by the length of each string in rlist in resverse order
        #Sorted(..)  => ['bb', 'a', 'y']
        #"".join(..) => 'bbay'
        return "".join(sorted(rlist, key=lambda x: len(x), reverse=True))

"""
Solution:
Utilize python collections.Counter() interface
collections.Counter() is a subclass of dict for counting hashable objects. It returns an unordered collection where elements are dictionary keys and their count are dictionary values.
"""
class Solution_2(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        r = "" # return string

        #c = Counter("baby") => Counter({ 'a':1, 'b':2, 'y':1})
        c = collections.Counter(s)

        #most_common([n]) returns a list of n most common elements and their counts in tuple from the most common to least. If n is ommited, return all elements in the counter. Basically it is a sorting utility for counter object to sort the counter by count
        # ex. c = Counter({'a':1, 'b':3, 'c':2})
        # c.most_common() => [ ('b', 3), ('c', 2), ('a', 1)]

        #a = c.most.common() => [('b',2), ('a',1), ('y',1)]
        l = c.most_common()
        for a in l:
            r += a[0] * a[1] 

        return r
"""
Test
"""
myTest = Solution_2()
print myTest.frequencySort("baby")
            
        
