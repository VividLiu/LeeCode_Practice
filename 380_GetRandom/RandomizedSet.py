"""
Solution: Using hash + list
Use a hashtable to store the (value, index) pair with value as key and its index in list as value. 
Thus, we can insert and remove in O(1) time. And since the index will be continuous number, we can get a random number between (0, n) and return the random value.
The problem is when we remove a value from hash, we need to remove that value from list too. How can we remove that value from list and shrink the list size in O(1) time.
The trick is when we remove some value from any location of the list, we can move the last element in list to fill the hole.
"""

class RandomizedSet(object):

    _debug = 0
    
    def __init__(self):
        """ 
        Initialize your data structure here.
        """
        self._set  = {}
        self._arr  = []
        self._size = 0 

        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self._debug:
            print "inserting ", val, " into set..."

        #the value already in set
        if val in self._set:
            return False


        #add {value:index} to set
        self._set[val] = self._size
        #add value into list 
        if self._size < len(self._arr):
            self._arr[self._size] = val
        else:
            self._arr.append(val)

        
        self._size += 1
        
        return True

        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self._debug:
            print "removing ", val, " from set..."
        
        #the value is not is set
        if val not in self._set:
            return False

        #remove it from list
        ind = self._set[val]
        self._arr[ind] = self._arr[-1]
        self._size -= 1 #decrement size
        #remove from set
        self._set.pop(val)

        #adjust the moved element index in set
        if self._arr[ind] in self._set:
            self._set[self._arr[ind]] = ind

        return True

        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self._debug:
            print "Getting a random number from ", self._arr

        ind = random.randint(0, self._size-1)
        return self._arr[ind]
       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
