"""
Solution:
Use a two poniter, front and back pointer.
The front moves from start while the back moves from end backwards. Comparing each character(disgard any non alphabetic character) while moving the two pointer at the same time until either mismatch or the two pointers meet at center of the string.
Note, the center of string can either be one character or two characters.
Ex. baab, front and back will meet at 'aa'
    bab, front and back will meet at 'a'
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #sanity check
        if len(s) == 0:
            return True
        
        front, back = 0, len(s)-1
        
        while front < back:
            #disgard any non alphabetic characters
            while not s[front].isalpha():
                front += 1
            while not s[back].isalpha():
                back -= 1
            
            if front >= back:
                break
            
            if s[front].lower() != s[back].lower():
                return False
            else:
                front += 1
                back  -= 1

        return True

"""
test
"""
myTest = Solution()

#testcase 1:
print "--------------------------"
print "tc1: s = '' ==> True"
print myTest.isPalindrome('')

#testcase 2:
print "--------------------------"
print "tc2: s = '' ==> True"
print myTest.isPalindrome('A man, a plan, a canal: Panama')

#testcase 3:
print "--------------------------"
print "tc3: s = '' ==> True"
print myTest.isPalindrome('A man, a plan, a cc anal: Panama')

#testcase 4:
print "--------------------------"
print "tc4: s = '' ==> True"
print myTest.isPalindrome('A man, a plan, a c...c anal: Panama')

#testcase 4:
print "--------------------------"
print "tc4: s = '' ==> True"
print myTest.isPalindrome('race a car')
