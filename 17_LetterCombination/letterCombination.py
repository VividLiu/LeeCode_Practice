"""
Method 1:
Use backtracking algorithm.
ex. digits  = '23'
    the backtracking tree is:
            root
       /     |      \
     a       b        c
   / | \   / | \    / | \
 ad ae af bd be bf cd ce cf  

The accpet(), reject(), generateNext() function for this backtracking algorithm is:
- accept(): when all digits are mapped to letter
- reject(): no need
- generateNext(): for current digit, go through all possible letters
"""
class Solution2(object):
    _debug = 0 
    #class variable, shared by class instances
    _phoneMP = { '1':'*',
                 '2':'abc',
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6':'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #sanity check
        if digits == "": 
            return []

        #
        combinations = []
        self.letterGenerator(digits, 0, "", combinations)

        return combinations

    #backtracking function
    #generate the possible letter for ith digit in digits and append it to result set
    def letterGenerator(self, digits, i, res, combinations):
        if self._debug:
            print "-------------------------"
            print "i: " + str(i) + ", res:" + res 

        #accept candidates
        if len(res) == len(digits):
            combinations.append(res)
            return

        #if haven't reach the accepting condition,
        #generate the next level candidates 
        for c in self._phoneMP[digits[i]]:
            self.letterGenerator(digits, i+1, res + c, combinations)
            
"""
Method 2:
Use python list comprehension(basically, two iterative loops)

Note about list comprehension
List comprehension are a tool for transforming one list into another list.
 - Conditional comprehensions
    ex. for n in numbers:
            if n%2 == 1:
                n*2
        ==> list comprehension representation
        [n*2 for n in numbers if n % 2 == 1]

 - Nested list comprehensions 
    ex. to flatten a matrix
        for row in matrix:
            for n in row:
                flat.append(n)
        ==> list comprehension representation
        [n for row in matrix for n in row ]
    note: when working with nested loops in list comprehensions, remember that the for clause remain in the same order as in our original for loops. The same rule also applies to set or dictionary comprehensions.

    python allows line breaks between brackets and braces to increase readability.
    ex. [ n*2 for n in numbers if n%2==1]
        ==> with breaks
        [
            n*2
            for n in numbers
            if n%2 == 1
        ]
    
"""

class Solution(object):
    _phoneMP = { '1':'*',
                 '2':'abc',
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6':'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        #sanity check
        if digits == "": 
            return []

    
        #return results
        res = [""]

    
        #for d in digits:
        #    tmp = []
        #    for r in res:
        #        for letter in self._phoneMP[d]:
        #            tmp.append(r + letter)
        #    res = tmp

        #list comprehension of above 'for' loops
        res = reduce(lambda acc, digit: [x+y for x in acc for y in self._phoneMP[digit]], digits, [''])

        return res 

"""
test
myTest = Solution()

#testcase 1):
print "-------------------------"    
print "tc1: digits = '23' => ['ad', 'ae', 'af', 'bd', 'bf', cd', 'ce', 'cf']"
print myTest.letterCombinations('23')
    
#testcase 2):
print "-------------------------"    
print "tc2: digits = '2' => ['a', 'b', 'c']"
print myTest.letterCombinations('2')

#testcase 3):
print "-------------------------"    
print "tc3: digits = '22' => ['aa','ab','ac','ba','bb','bc','ca','cb','cc']"
print myTest.letterCombinations('22')
"""


