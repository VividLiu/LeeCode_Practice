class Solution(object):
    """
    Method 2:
    See question.txt for detail explanation
    """
    def countBits(self, num):
        #return list, containing result for 0 in advance
        res = [0] 

        for i in xrange(1, num+1):
            res.append((i & 1) + res[i >> 1]);

        return res;

    """
    Method 1:
    Divide current problem N into two sub problems.
    The highest 1 bit and the remaining.
    Ex. 0b10111 => 0b10000 + 0b111
    """
    def countBits_2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        #return list, containing result for 0 in advance
        res = [0] 

        for i in xrange(1, num+1):
            binary = bin(i)
            l = len(binary) - 2 # get the highest one bit position 
            rem = i - (1 << (l-1)) # 1 << (l-1) is equal to power(2, l-1), which is the highest 1 bit part

            #debug
            #print "-------------------"
            #print "num: " + str(i)
            #print "power: " + str(pow(2, l-1))
            #print "rem: " + str(rem)

            res.append(1 + res[rem]);

        return res;
