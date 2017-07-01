"""
Solution:
Use stack to track. 
If it is '.', no change of current stack.
If it is '..', pop the top element out, since it goes back one level
If it is others, push the directory into stack
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        #Ex. '/a/b/../c//d/' => ['', 'a', 'b', '..', 'c'.'', 'd', '']
        dirs = path.split("/") 

        for i in xrange(len(dirs)):
            if dirs[i] == '..':
                if stack:
                    stack.pop()
            elif dirs[i] == '.' or dirs[i] == "":
                continue
            else:
                stack.append(dirs[i])

        return "/" + "/".join(stack)
                
