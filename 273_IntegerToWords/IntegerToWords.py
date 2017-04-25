class Solution(object):
    _debug = 0

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        #edge case 
        if num == 0:
            return "Zero"

        #return string
        r = ""

        mp = { 0:"", 1:"Thousand", 2:"Million", 3:"Billion"} 

        i = 0
        while num:
            if self._debug:
                print "-------------------------------"
                print "remainder: " +  str(num % 1000)
                print "rest: " + str(num / 1000) 

            portion = num % 1000
    
            word = ""
            postfix = ""
            if portion != 0: #if portion is not 0
                word = self.portionConvert(portion) 
                postfix = mp[i]
                r = (word + " " + postfix + " ") + r

            num = num / 1000

            i += 1
        return r
            
    #--------------------------------------------------------------------------------
    # function poritonConvert(self, portion)
    # convert a number to an English words, the number is defined as a portion,
    # which means it is minimum 1 digit and maximum 3 digits.
    # ex. 123 => one hundred and twenty three
    #--------------------------------------------------------------------------------
    def portionConvert(self, p):
        """
        :type portion: int
        :rtype: str
        """
        #the speical numbers that need to be stored is hash table for convertion
        word_mp = { 1: 'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}

        #sanity check
        #if len(str(p)) > 3 or len(str(p)) < 1:
        if p > 999:
            print "it is not a portion"
            return ""
    
        #return result
        r = ""

        #if the third digit exists, convert it
        d3 = p / 100
        if d3: 
            r += word_mp[d3] + " Hundred"        
            #update p to remove the 3rd digit
            p = p % 100 

            if self._debug:
                print "3rd digit exists:"
                print "word: " + r

         
        #if the second digit exists, convert it
        d2 = p / 10
        if d2: 
            if self._debug:
                print "2nd digit exists:"

            if p in word_mp: #if these two digit (ex, 15) already exists in mp, it is a special case, otherwise it is normal one (ex, 23)
                r += (" " + word_mp[p] if r != "" else word_mp[p])
            else:
                #get the last single digit, since number like 20, 30..90 is already in mp, thus the last digit won't be 0
                p = p % 10
                r += (" " + word_mp[d2*10] + " " + word_mp[p] if r != "" else word_mp[d2*10] + " " + word_mp[p])

            if self._debug:
                print "word:" + r
        elif p: #only one digit and it is not 0
            r += (" " + word_mp[p] if r != "" else word_mp[p])

        if self._debug:
            print "     In portionConvert() function"
            print "     Return poriton word is " + r

        return r
        
"""
test
""" 
myTest = Solution()

#testcase 1):
print "--------------------------------"
print "tc1: 0 => 'Zero'"
print myTest.numberToWords(0)

#testcase 2):
print "--------------------------------"
print "tc2: 10 => 'Ten'"
print myTest.numberToWords(10)
            
#testcase 3):
print "--------------------------------"
print "tc3: 100 => 'One Hundred'"
print myTest.numberToWords(100)

#testcase 4):
print "--------------------------------"
print "tc4: 1,000 => 'One Thousand'"
print myTest.numberToWords(1000)

#testcase 5):
print "--------------------------------"
print "tc5: 3,000,100 => 'Three Million One Hundred'"
print myTest.numberToWords(3000100)

#testcase 6):
print "--------------------------------"
print "tc6: 3,000,001 => 'Three Million One'"
print myTest.numberToWords(3000001)

#testcase 7):
print "--------------------------------"
print "tc7: 999,999,999 => 'Nine Hundred Ninty Nine Million Nine Hundred Ninty Nine Thousand Nine Hundred Ninty Nine'"
print myTest.numberToWords(999999999)

#testcase 8):
print "--------------------------------"
print "tc8: 4,123,456,789 => 'Four Billion One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine'"
print myTest.numberToWords(4123456789)

#testcase 9):
print "--------------------------------"
print "tc9: 19 => 'Nineteen'"
print myTest.numberToWords(19)
