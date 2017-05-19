#readd4 API is already defined for you.
# # @param buf, a list of characters
# @return an integer
def read4(buf):
    for i in xrange(4):
         buf[i] = '0'
    return 4
 
class Solution(object):
     def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        #index of current point in return buffer that needs to be wrote
        idx = 0
        
        while idx < n:
            #initialize the destination buffer for read4 api
            buf4 = [ "" for i in xrange(4)]
            
            #read maximumly 4 characters into the buffer
            #read_num is actually number of characters read from buffer.
            read_num = min(read4(buf4), n-idx)
            
            for i in xrange(read_num):
                buf[idx] = buf4[i]
                idx += 1
            
            if read_num < 4:
                break
        
        return idx
            
"""
test
"""
myTest = Solution()
buf = [ "" for i in xrange(10)]
print buf
print myTest.read(buf, 9)
print buf
