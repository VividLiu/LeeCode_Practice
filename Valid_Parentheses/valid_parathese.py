#usr/bin/python

"""
sudo code:
	iterate s from left to right
		if any right parenthese is encountered
			return false;
		if any left parenthese is encountered
			start iterating from right to left
				if the corresponding right parenthese is encountered
					truncate the string so that only the part between the encountered parenthese is left;
					call it new_s;
					then recursively call the same steps for new_s;
					return the result;
				if wrong or no right parenthese is encountered
					return false;
"""
class Solution:
	# @return a boolean
	def isValid(self, s):
		for i in range(0, len(s)):
			if s[i] in ")]}":
				#print "debug 1"
				#single right parenthese encountered
				return False
			elif s[i] in "([{":
				#print "debug 2"
				for j in range(len(s)-1 , -1, -1):
					if s[j] in ")]}":
						if ( s[i] == '(' and s[j] == ')' ) or ( s[i] == '[' and s[j] == ']' ) or ( s[i] == '{' and s[j] == '}'):
							new_s = s[i+1:j]
						  	print "new string: " + new_s
							return self.isValid(new_s)
						else:
							#left and right parentheses don't match
							return False
				#single left parenthese encountered
				return False
		#no parathese left
		#print "debug 3"
		return True

#test
my_solution = Solution()
#open a file
infile = open("testcase.txt", 'r')

for line in infile:
	print line

	print my_solution.isValid(line)
#close a file
infile.close()



