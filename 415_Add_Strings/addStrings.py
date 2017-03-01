class Solution(object):
    """
    Extract one digit from both string and convert to int to add
    When one string reach end, use 0 instead.
    """
    def addStrings(self, num1, num2):
        """
        :type num1: str, len(num1) < 5100
        :type num2: str, len(num2) < 5100
        :rtype: str
        """

        #reverse strings
        rNum1 = num1[::-1]
        rNum2 = num2[::-1]
    
        c = 0       #carrier
        i = 0       #pointer
        sum = ""    #adding result in string
        l = len(num1) if len(num1) >= len(num2) else len(num2) #length of longer string

        while(i < l or c!= 0):
            #adding 0s to the shorter string for adding convenience
            d1 = 0 if i >= len(rNum1) else rNum1[i]
            d2 = 0 if i >= len(rNum2) else rNum2[i]

            #adding
            res = int(d1) + int(d2) + c

            #calculating carrier, remainder
            c, res = res // 10, res % 10

            sum = str(res) + sum
            i += 1
        
        return sum

    """
    Extract maximum 9 digits from both string and convert to int to add
    This version still has some unsolved bug
    """
    def addStrings_2(self, num1, num2):
        """
        :type num1: str, len(num1) < 5100
        :type num2: str, len(num2) < 5100
        :rtype: str
        """

        #reverse strings
        rNum1 = num1[::-1]
        rNum2 = num2[::-1]
        
        c = 0       #carrier
        result = "" #adding result

        while rNum1 and rNum2:
            #since the maximum 32 bit integer is 10 digit 2147483647
            #we add 9 digit number each time to avoid overflow
            subNum1 = rNum1[:9] if (len(rNum1) > 9) else rNum1
            subNum2 = rNum2[:9] if (len(rNum2) > 9) else rNum2

            #get the rest part 
            rNum1 = rNum1[9:] if (len(rNum1) > 9) else ""
            rNum2 = rNum2[9:] if (len(rNum2) > 9) else ""

            #debug
            print "-----------"
            print "subNum1: " + subNum1[::-1]
            print "subNum2: " + subNum2[::-1]
            print "carrier: " + str(c)
            print "rNum1:"    + rNum1
            print "rNum2:"    + rNum2
            

            #add operation
            tmp = int(subNum1[::-1]) + int(subNum2[::-1]) + c

            #debug
            print "tmp" + str(tmp)
            
            if(tmp > 999999999): #if the result overflows to 10 digits
                #get the carrier
                c = tmp // 1000000000
                tmp = str(tmp)[1:]
            else:
                c = 0
                tmp = str(tmp)

            #concatenate the result
            result = tmp + result

            #debug
            print "current result: " + result
    

        #concatenate the rest of unfinished string 
        Num = rNum1 if rNum1 else ( rNum2 if rNum2 else "")
        while Num:
            subNum = Num[:9] if (len(Num) > 9) else Num
            Num = Num[9:] if (len(Num) > 9) else ""

            tmp = int(subNum[::-1]) + c

            #debug
            print "-------------------"
            print "subNum: " + subNum[::-1]
            print "Carrier: "+ str(c)
            print "Num: "    + Num

            if(tmp > 999999999):
                c = tmp // 1000000000
                tmp = str(tmp)[1:]
            else:
                c = 0  
                tmp = str(tmp)
                
            result = tmp + result

            #debug
            "current result: " + result

        if c != 0:
            result = str(c) + result
            #debug
            print "------------------"
            print "remaining carrier: " + str(c)
            print "current result: " + result
 

        return result
            

"""
test
"""
myTest = Solution()
#print myTest.addStrings("0", "0")
#print myTest.addStrings("1", "2")
#print myTest.addStrings("1234567", "9")
#print myTest.addStrings("1234567", "123456789")
print myTest.addStrings("38579237592375923", "23452524243")

            
            

    
