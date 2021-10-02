
"""
Version_3:

Thinking:
	Version_2 fails at example: "([)]": p1 = 1, p2 = 1, p1 = 0, p2 = 0
To correct it, we need to add a prerequisite to version_2's algorithm.
That is, if p1 increased first, then p2 is increased.
p2 has to decrease to 0 before p1 so that no wrong nesting happens

Algorithm:
	use a stack to track which parathese is the last one in the nest
"""
class Solution:
	# @return a boolean
	def isValid(self, s):

		stack = []

		for letter in s:
			if letter in "({[]})":
				if letter == "(":
					stack.append("(")
				elif letter == "{":
					stack.append("{")
				elif letter == "[":
					stack.append("[")

				if letter == ")":
					if not stack:
						return False
					elif stack[len(stack)-1] == "(":
						stack.pop()
					else:
						stack.append(")")
				elif letter == "}":
					if not stack:
						return False
					elif stack[len(stack)-1] == "{":
						stack.pop()
					else:
						stack.append("}")					
				elif letter == "]":
					if not stack:
						return False
					elif stack[len(stack)-1] == "[":
						stack.pop()
					else:
						stack.append("]")
			# print stack	

		if not stack:
			return True
		else:
			return False

#test
my_solution = Solution()

#open a file
infile = open("testcase.txt", 'r')

cnt = 1
for line in infile:
	print
	print cnt
	print "test input: " + line,"output: ",my_solution.isValid(line)

	cnt += 1
#close a file
infile.close()
