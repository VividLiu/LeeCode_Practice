class Solution(object):
    def countAndSay(self, n): 
        """
        :type n:  int
        :rtype :  str
        """
        i = 1 
        cur = '1' 
        while i < n:
            cur = self.say(cur)
            i += 1

        return cur 
    

    # given a str of integers, return its next str
    # ex. say('222344') => '321324'
    # @param num: str of integers. ex. '1211'
    # @return param: a string
    def say(self, num):
        res = ""
        cnt = 1 
        for i in xrange(len(num)):
            if (i == len(num)-1) or (num[i] != num[i+1]):
                res += str(cnt) + num[i]    
                cnt = 1 
            else:
                cnt += 1 
    
        return res 
