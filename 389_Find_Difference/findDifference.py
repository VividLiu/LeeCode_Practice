"""
Method 1:
Similar to find single number in an array which all the rest duplicates.
Just convert the character to ascII 
"""
class Solution_1(object):
    def findTheDifference(self, s, t): 
        """
        :type s: str
        :type t: str
        :rtype: str
        """

            
        #concatenate two strings into one
        a = s + t 

        #loop through the each character in the concatenated string
        #get the ASCII number of each character and do xor
        #xor will cancel out duplicates
        #thus, the result will be the ASCII number of the single char
        r = 0 
        for c in a:
            r ^= ord(c) # ord('a') => 97  

        return chr(r) # chr(97) => 'a' 
        
"""
Method 2:
Since the duplicates are separated into two string array, we can simpley sum up all the ascii of the characters in both s and t, and do a subtraction to get the ascii of the extra character
"""
class Solution(object):

    def findTheDifference(self, s, t): 
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        #Use reduce() to sum ascii number of all chars in s
        #with initailizer be 0 since s can be empty string
        sum_s = reduce(lambda x, y: x + ord(y), list(s), 0)

        sum_t = reduce(lambda x, y: x + ord(y), list(t), 0)

        return chr(sum_t - sum_s)

"""
test
myTest = Solution()

print "testcase: s:'', t: 'e'"
print myTest.findTheDifference("", "e")

print "testcase: s:'abc', t:'cbae'"
print myTest.findTheDifference("abc", "cbae")


print "testcase: s:'abcc', t:'cbadc'"
print myTest.findTheDifference("abcc", "cbadc")
"""

