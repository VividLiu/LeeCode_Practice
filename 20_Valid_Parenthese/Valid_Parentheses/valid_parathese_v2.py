#!usr/bin/python

"""
version_2:
Thinking:
	What about (xxx)(xxx), (xxx){xxx}? The first version fails this sample.

algorithm:
	initialize three int type variables for (, {, [ separately.
	When any left parenthese is encountered, the corresponding variable is increased by 1.
	When any right parenthese is encountered, the corresponding variable is decreased by 1.
	Whenever one of the three variables is less than 0, the expression is not valid.
"""
class Solution:
	# @return a boolean
	def isValid(self, s):
		#three variables to count for the appearance of (, {, [
		p1 = 0
		p2 = 0
		p3 = 0

		for letter in s:
			if letter in "({[]})":
				if letter == "(":
					p1 += 1
				elif letter == ")":
					p1 -= 1
				elif letter == "{":
					p2 += 1
				elif letter == "}":
					p2 -= 1			
				elif letter == "[":
					p3 += 1
				elif letter == "]":
					p3 -= 1

				#check
				if (p1 < 0) or (p2 < 0) or (p3 < 0):
					return False

		if (p1 == 0) and (p2 == 0) and (p3 == 0):
			return True		
		else:
			return False

#test
input_string = raw_input("Enter the test string: ")

my_solution = Solution()
print my_solution.isValid(input_string)

