"""
Solution:
First note that least recently used != least used.
Least used means the one with lowest usage frenquency, while least recently used means the oldest one in the timeline that was used. 
Thus, for evicting the least used key, whenever a key was just used, it is the put to the end of the datastructure to remove since it is most recently used key. 
To fulfill this O(1) requirement, we need a datastructe that allows us to do inserting/deleting an element in O(1) time. 
Double link list is the choice since for each node, it has a pointer to previous node and a pointer to next node. So it only takes O(1) time for inserting and deleting.
To compare, a single link list takes O(n) time for inserting and deleting a node since it only contians the pointers to next element, it needs O(n) time to iterate through the list and find the preceding node of the node to be removed or the locaiton to be inserted. 
"""
class ListNode():
    def __init__(self, key, value):
        self.key    = key
        self.value  = value
        self.prev   = None
        self.next   = None

class LRUCache2(object):
    _debug = 1

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity           #the capacity of the cache
        self._size     = 0                  #size of current cache
        self._hash     = {}                 #initialize the hash table with key as key, and its value, its corresponding linked list node reference as value.
        self._head     = ListNode(-1, -1)   #the head reference to double link list, use a special node as head
        self._tail     = None               #the tail reference to double link list
    
        if self._debug:
            print "----------------------"
            print "A new LRU cache was initialized with capacity = ", capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self._debug:
            print "getting value for key = ", key

        if key in self._hash:
            #update its location in list so it become the most recent used key
            self._remove(self._hash[key][1])
            self._addHead(self._hash[key][1])
            
            if self._debug:
                print "     the current hash is ", self._hash
                print "     the current tail node is ", self._tail.key
            return self._hash[key][0]
        else:
            if self._debug:
                print "     the current hash is ", self._hash
                print "     the current tail node is ", self._tail.key
            return -1
        
     

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._debug:
            print "putting {" + str(key) + ":" + str(value) + "} into cache..." 
        if key not in self._hash:#add a new key in cache
            if self._size == self._capacity:#need to evict one LRU key which is in the tail of list to get space for new key
                #remove tail node
                LRUkey = self._popTail()
                #remove key from hash
                self._hash.pop(LRUkey) 
                #reduce size
                self._size -= 1
                
            #add new key in hash table
            newNode = ListNode(key, value)
            self._hash[key] = (value, newNode)
            #add new node in the head of list
            self._addHead(newNode)
            #increase size
            self._size += 1
        else: #if value is not same, 
            if value != self._hash[key][0]:
                #remove (key, old value)
                self._remove(self._hash[key][1])
                self._hash.pop(key) 
                #add (key, new value)
                newNode = ListNode(key, value)
                self._hash[key] = (value, newNode)
                #add new node in the head of list
                self._addHead(newNode)

        if self._debug:
            print "     the current hash is ", self._hash
            print "     the current tail node is ", self._tail.key
  

    #remove the tail node from the linked list
    def _popTail(self):
        if self._debug:
            print "     removing tail node..."
        if self._tail:
            key = self._tail.key
            prev = self._tail.prev
            prev.next = None    

            self._tail.prev = None

            if prev != self._head:
                self._tail = prev
            else:
                self._tail = None

            if self._debug:
                print "     key = " + str(key) + " node is removed from tail"
            
            return key
        return -1
    
    #add a node in the head of the linked list
    # @param node: the node to be inserted in head of link list    
    def _addHead(self,node):
        nextNode = self._head.next

        node.prev = self._head
        node.next = nextNode
        
        if nextNode:
            nextNode.prev = node
        else: #the list is empty, adding the first node, update tail pointer
            self._tail = node

        self._head.next = node

        if self._debug:
            print "     a new node key=" + str(node.key) + " is added in head of list"

    #give a node reference, remove the node from list
    # @param node: node reference
    def _remove(self,node):
        prev = node.prev
        next = node.next

        prev.next = next
        if next:
            next.prev = prev
        else: #node is the last node in list, which is the _tail node, update _tail
            if prev != self._head:
                self._tail = prev
            else: #node is the only node in list
                self._tail = None  

        node.prev = None
        node.next = None

        if self._debug:
            print "     a node key=" + str(node.key) + " is removed from the list"
        
"""
Few optimization of above solution:
1). Set _head, _tail poniter as a dummy node can avoid the consideration of some annoying edge cases. 
"""
class LRUCache(object):
    _debug = 1

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity           #the capacity of the cache
        self._size     = 0                  #size of current cache
        self._hash     = {}                 #initialize the hash table with key as key, and its value, its corresponding linked list node reference as value.
        self._head     = ListNode(-1, 'head')   #the head reference to double link list, use a dummy node as head
        self._tail     = ListNode(-1, 'tail')   #the head reference to double link list, use a dummy node as head
        
        #link _head and _tail
        self._head.prev = None
        self._head.next = self._tail
        self._tail.prev = self._head
        self._tail.next = None
    
    
        if self._debug:
            print "----------------------"
            print "A new LRU cache was initialized with capacity = ", capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self._debug:
            print "getting value for key = ", key

        if key in self._hash:
            #update its location in list so it become the most recent used key
            self._remove(self._hash[key][1])
            self._addHead(self._hash[key][1])
            
            if self._debug:
                print "     the current hash is ", self._hash
            return self._hash[key][0]
        else:
            if self._debug:
                print "     the current hash is ", self._hash
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._debug:
            print "putting {" + str(key) + ":" + str(value) + "} into cache..." 
        if key not in self._hash:#add a new key in cache
            if self._size == self._capacity:#need to evict one LRU key which is in the tail of list to get space for new key
                #remove tail node
                LRUkey = self._popTail()
                #remove key from hash
                self._hash.pop(LRUkey) 
                #reduce size
                self._size -= 1
                
            #add new key in hash table
            newNode = ListNode(key, value)
            self._hash[key] = (value, newNode)
            #add new node in the head of list
            self._addHead(newNode)
            #increase size
            self._size += 1
        else: #if value is not same, 
            if value != self._hash[key][0]:
                #remove (key, old value)
                self._remove(self._hash[key][1])
                self._hash.pop(key) 
                #add (key, new value)
                newNode = ListNode(key, value)
                self._hash[key] = (value, newNode)
                #add new node in the head of list
                self._addHead(newNode)

        if self._debug:
            print "     the current hash is ", self._hash

    #remove the tail node from the linked list
    #call _remove inside
    # @return param: int, the key of the poped node, -1 if no node is popped
    def _popTail(self):
        if self._debug:
            print "     removing tail node..."

        #no node in link list
        if self._tail.prev == self._head:
            if self._debug:
                print "     Empty list, no node to be removed."
            return -1

        rkey = self._tail.prev.key
        self._remove(self._tail.prev)
        return rkey

    #add a node in the head of the linked list
    # @param node: the node to be inserted in head of link list    
    def _addHead(self,node):
        nextNode = self._head.next
        nextNode.prev = node
        self._head.next = node

        node.prev = self._head
        node.next = nextNode

        if self._debug:
            print "     a new node key=" + str(node.key) + " is added in head of list"

    #give a node reference, remove the node from list
    # @param node: node reference
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None
         
        if self._debug:
            print "     a node key=" + str(node.key) + " is removed from the list"
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
test
"""
obj = LRUCache(2)

obj.put(1,1)

obj.put(2,2)

print obj.get(1)

obj.put(3,3)

print obj.get(2)

