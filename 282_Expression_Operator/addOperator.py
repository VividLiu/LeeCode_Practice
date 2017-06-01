#------------------------------------------------------------------------------------------
#backtracking
#To simpley this question, let's assume num is a list[int], thus, no need to worry about the 
#different combinations of numbers the num string can generate
#The only difficulty is when encounter *, we need to back step one operands to calculate the
#current result, since * has higher precedence than +/-, wo the order of calculation changes,
#and a*b need to be calcualted first.
#------------------------------------------------------------------------------------------
class Solution_simplified(object):
    _debug = 0
    
    def addOperators(self, num, target):
        """
        :type num: list[int]
        :type target: int
        :rtype: List[str]
        """
        
        #sanity check
        if len(num) == 0:
            return []
        
        #return list
        res = []
        
        self.bt(num, 0, num[0], target, "", res)
        
        return res

    def bt(self, num, ind, culmRes, target, opSeq, res):
        """
        :type num: array, array of operands, ex. [1,0,5]
        :type ind: int, index of current operands
        :target: int
        :opSq: str, operator sequence. ex. '*+'
        :res: list of all possible operation results ['1*0+5']
        """
        if self._debug:
            print "ind: " + str(ind) + ", current cumulative result: " + str(culmRes) + " current opperator sequence: ",
            print opSeq
            
        #sanity check
        if len(num) == 0:
            print "error: empty operands array"
            return 0
        
        if ind >= len(num):
            print "error: index out of operands array, ind=" + str(ind)
            return 0
        
        #reach the end of operands
        if ind == len(num) - 1:
            if culmRes == target:
                #accpet current candidate as one valid solution
                res.append(self.operations(num, opSeq))
                return 1
            else:
                #reject current candidate
                return 0
                
        
        #generate next level of candidates
        #advance ind
        ind += 1
        for op in "+-*":
            if op == "+":
                self.bt(num, ind, culmRes + num[ind], target, opSeq + "+", res)
            if op == "-":
                self.bt(num, ind, culmRes - num[ind], target, opSeq + "-", res)
            if op == "*":
                #if the current operator is *, the order of operation won't be simpley
                #from left to right anymore, since * has higher precedence than +/-
                #thus we need to change the order of operatoin and calculate the a*b first
                newCulm = 0 #the current cumulative result
                preOp = opSeq[-1] if len(opSeq) > 0 else "" #the previous operator, return "" if there is no previous operator which means the current operator is the first one
                
                if preOp == '+':
                    newCulm = culmRes - num[ind-1] + num[ind-1] * num[ind]
                elif preOp == '-':
                    newCulm = culmRes + num[ind-1] - num[ind-1] * num[ind]
                elif preOp == '*' or preOp == "":
                    newCulm = culmRes * num[ind]
                else:
                    print "error: unexpected operator " + preOp
                
                self.bt(num, ind, newCulm, target, opSeq + "*", res)
                

    def operations(self, num, opArr):
        """
        :type num: arrary, array of operands, ex. [1,2,3]
        :type opArr: str, str of operators, ex. '++'
        :rtype: str ex. '1+2+3'
        """
        
        res = str(num[0])
        
        #sanity check
        if len(num) == 0 or len(opArr) == 0:
            print "error: num or opArr is empty"
            return ""
        
        if len(num) != len(opArr) + 1:
            print "error: length error"
            return ""
        
        for i in xrange(len(opArr)):
            res += opArr[i]
            res += str(num[i+1])
        
        return res

#---------------------------------------------------------------------------------------------
# Solution for full version of the question
# The difference compared to simplied version solution is that when generating next level of 
# operators, also generate different possible operands for the current operand
#---------------------------------------------------------------------------------------------
class Solution(object):
    _debug = 0
    
    def addOperators(self, num, target):
        """
        :type num    : str
        :type target : int
        :rtype       : List[str]
        """
        #sanity check
        if len(num) == 0:
            return []
        
        #return list
        res = []
        
        for i in xrange(1, len(num)+1):
            #num[:i] as the first operand
            operand = int(num[:i])
            self.bt(num, i, operand, operand, target, num[:i], res)
            
            #the int can not start with 0, ex. 0123, thus, the only valid first operand is '0'
            if i == 1 and num[0] == '0':
                break
        
        return res
    
    
    def bt(self, num, ind, mulRes, cumRes, target, opSeq, res):
        """
        :type num    : str
        :type ind    : int, starting index in num string of next operand
        :type mulRes : multiple level result, ex. "1+2+3*4*5 => mul=3*4*5=60"
        :type cumRes : current operation result, ex"1+2+3*4*5=> cumRes=63"
        :target      : int
        :opSq        : str, operation sequence. ex. '1*0+5'
        :res         : list of all possible operation results ['1*0+5']
        """
        if self._debug:
            print "ind: " + str(ind) + ", current cumulative result: " + str(culmRes) + " current opperator sequence: ",
            print opSeq
            
        #sanity check
        if len(num) == 0:
            print "error: empty operands array"
            return 0
        
        if ind > len(num):
            print "error: index out of operands array, ind=" + str(ind)
            return 0
        
        #reach the end of operands
        if ind == len(num):
            if cumRes == target:
                #accpet current candidate as one valid solution
                res.append(opSeq)
                
                if self._debug:
                    print "accept current branch " + opSeq
                return 1
            else:
                #reject current candidate
                if self._debug:
                    print "reject current branch " + opSeq
                return 0
                
        
        #generate next level of candidates
        #advance ind
        for i in xrange(ind+1, len(num) + 1):
            #next oprand is int(num[ind:i])
            operand = int(num[ind:i])
            
            for op in "+-*":
                if op == "+":
                    self.bt(num, i, operand, cumRes + operand, target, opSeq + "+" + num[ind:i], res)
                if op == "-":
                    self.bt(num, i, -operand, cumRes - operand, target, opSeq + "-" + num[ind:i], res)
                if op == "*":
                    #if the current operator is *, the order of operation won't be simpley
                    #from left to right anymore, since * has higher precedence than +/-
                    #thus we need to change the order of operatoin and calculate the a*b*c*d... first
                    self.bt(num, i, mulRes * operand, cumRes - mulRes + mulRes * operand, target, opSeq + "*" + num[ind:i], res)
                    
            #no int can start with 0, ex. 0123, except 0 itself
            #thus the next operand can only be 0
            if i == (ind+1) and num[ind] == '0':
                break
"""
test for simplified question
myTest_simplified = Solution_simplified()

print myTest_simplified.addOperators([1,2,3], 6)
print myTest_simplified.addOperators([2,3,2], 8)
print myTest_simplified.addOperators([1,0,5], 5)
print myTest_simplified.addOperators([0 ,0], 0)
"""
            
"""
test
"""

myTest = Solution()
print myTest.addOperators("123", 6)
print myTest.addOperators("232", 8)
print myTest.addOperators("105", 5)
print myTest.addOperators("00", 0)
print myTest.addOperators("1234", 25)

        
