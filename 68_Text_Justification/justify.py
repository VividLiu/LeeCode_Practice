class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        lines = [[]]
         
        #put as many as possible word in each line
        for word in words:
            #the reduce() line will sum up the characters of each word in current line
            # 1 is for the space between word
            if reduce(lambda l, w: l + len(w) + 1, lines[-1], -1) + len(word) + 1 <= maxWidth: #the current line can accomodate the coming word
                lines[-1].append(word)
            else: #start new line
                lines.append([word])
        
        #distribue space to each word 
        for i, line in enumerate(lines):
            spaces = maxWidth - reduce(lambda l, w: l + len(w), line, 0)
            #print i, "th line has ", spaces, " spaces"
            
            #if this line only contains one word
            #left justified; append extra space at the end of last word
            if len(line) == 1:
                line[-1] += " " * spaces
            elif i == len(lines) - 1: #if it last line, need to append " " to break each word
                for j in xrange(0, len(line) - 1):
                    line[j] += " "    
                line[-1] += " " * (spaces - len(line) + 1)
            else:
                evenSpaces = spaces / (len(line)-1)
                extraSpaces = spaces % (len(line)-1)
                
                #print evenSpaces
                #print extraSpaces
                
                for j in xrange(0, len(line)-1):
                    line[j] += " " * (evenSpaces + 1) if j < extraSpaces else " " * evenSpaces
                    
        #print lines
        return map(lambda l: "".join(l), lines)
                    
                
                

"""
test
"""
myTest = Solution()
print myTest.fullJustify(['it', 'is', 'a', 'beautiful', 'day'], 10)
print myTest.fullJustify(['i', 't', 'is', 'a', 'beautiful', 'day'], 10)
print myTest.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print myTest.fullJustify(["Here","is","an","example","of","text","justification."]
,14)
