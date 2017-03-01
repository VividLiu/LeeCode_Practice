class Solution(object):

    """
    Optimization of findWords_2.
    Use array of strings as data structure instead.
    keyboard = ["QqWwEeRrTtYyUuIiOoPp", "AaSsDdFfGgHhJjKkLl", "ZzXxCcVvBbNnMm"]
    And use "in" build in function to see if the letter is in special row.
    """
    def findWords(self, words):
        #return list
        rlist = []

        #define structure for keyboard
        keyboard = ["QqWwEeRrTtYyUuIiOoPp", "AaSsDdFfGgHhJjKkLl", "ZzXxCcVvBbNnMm"]

        for word in words:
            flag = True

            #retrieve the row number of first letter of current word
            row = 0 if word[0] in keyboard[0] else (1 if word[0] in keyboard[1] else 2)                       #check if the rest letters in the same row
            for letter in word[1:]:
                if letter not in keyboard[row]:
                    flag = False
                    break
    
            if flag:
                rlist.append(word)
    

        return rlist

    """
    Use dictionary to store the the row number for each letter.
    """
    def findWords_2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #return list
        rlist = []

        #create a dictionary structure to record row number of each letter
        keyboard = {'Q': 0, 'W':0, 'E':0, 'R':0, 'T':0, 'Y':0, 'U':0, 'I':0, 'O':0, 'P':0, 'A':1, 'S':1, 'D':1, 'F':1, 'G':1, 'H':1, 'J':1, 'K':1, 'L':1, 'Z':2, 'X':2, 'C':2, 'V':2, 'B':2,'N':2, 'M':2};


        #iterate through each word
        for word in words:
            prerow, row = -1, -1 #row number of previous letter, 
                                 #row number of current letter
                                 
            if(len(word) > 1):
                #iterate through each letter in current word
                for letter in word:
                    row = keyboard[letter.upper()]

                    if(prerow != -1 and row != prerow):
                        break
                    prerow = row
                else: #this statement got executed only when the for loop terminates through exhausion of the list
                    rlist.append(word)
            else: #special case: one letter word
                rlist.append(word)
                

        return rlist
