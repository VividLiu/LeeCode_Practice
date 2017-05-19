# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
fileCtx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
pointer = 0
def read4(buf):
    #if no global keyword, can only read global variable outside of function enclosing scope. With global keyword, can actually modify the value of global variable
    global pointer
    i = 0
    for i in xrange(min(4, len(fileCtx)-pointer)):
        buf[i] = fileCtx[pointer]
        pointer += 1
    return i+1
     
"""
This question is similar to 157.Read N Characters Given Read4. The only difference is that read() can be called multiple times. What does that really mean is that, 
for example you have four characters 'a', 'b', 'c', 'd' in file, when you call read() twice
read(buf, 1) should return 'a'
read(buf, 3) should return 'b'
The tricky part is that when you call api read4(), it will read all 4 into buffer while you only want to read 1, thus, how to preserve the over read characters. 
"""
class Solution(object):
    #the global temporary buffer which is used to store the over readed characters from previous read4() call
    def __init__(self):
        self._tmpBuf = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        #index of current buffer position to be written
        idx = 0
        
        #if _tmpBuf is not empty, read characters from _tmpBuf first, then call read4() api to read rest characters from file
        for i in xrange(min(len(self._tmpBuf), n)):
            buf[idx] = self._tmpBuf.pop(0)
            idx += 1
            
        while idx < n:
            #initialize the buffer for read4() api
            buf4 = ['', '', '', '']
            
            numRead = read4(buf4)
            print "read4 api:"
            print buf4
            print numRead
            
            #the number of rest characters need to be read 
            needToRead = n-idx
            
            for i in xrange(min(numRead, needToRead)):
                buf[idx] = buf4[i]
                idx += 1
            
            #update _tmpBuf
            if needToRead < numRead:
                for i in xrange(needToRead, numRead):
                    #until this point, _tmpBuf must be empty, thus no need to clear
                    self._tmpBuf.append(buf4[i])
               
            
            #nothing more to read, the actual number of characters read might be smaller than n if there is not enough to read from file
            if numRead < 4:
                #end reading
                break
        return idx

"""
test
"""
myTest = Solution()
#testcase 1):
print "-------------------------"
n = 2
buf = [ "" for i in xrange(n)]
print myTest.read(buf, n)
print "the characters read into buffer"
print buf
#testcase 2):
print "-------------------------"
n = 0
buf = [ "" for i in xrange(n)]
print myTest.read(buf, n)
print "the characters read into buffer"
print buf
