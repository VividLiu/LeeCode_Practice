"""
sudo code:
	initialize two pointer A_it, B_it pointing to start of A and B respectively,
	
	while A_it and B_it are not reaching the end of the list
		if *A_it > *B_it
			insert *B_it before *A_it
			increment A_it
			increment B_it
		if *A_it <= *B_it
			increment A_it
	if A_it is reaching the end
		add the rest of B to the end of A
	if B_it is reaching the end
		nothing

time complexity:
	O(m+n)
"""
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
    	A_it = 0
    	B_it = 0

    	#empty list test
    	if len(A) == 0: #A is empty
    		print "A is empty"
    		for i in range(B_it, n):
    			A.insert(len(A), B[i])
    		return

    	if len(B) == 0:
    		print "B is empty"
    		return

    	while (A_it < len(A)) and (B_it < n):
    		if A[A_it] > B[B_it]:
    			A.insert(A_it, B[B_it])
    			print "inserting.. ", B[B_it]
    			A_it += 1
    			B_it += 1
    		elif A[A_it] <= B[B_it]:
    			A_it += 1

    	if A_it == len(A):
    		for i in range(B_it, n):
    			A.insert(len(A), B[i])

#----------------------------------------------
#test

#case 1
# A = [1,3,4,6,8,10]
# B = [2,4,5,7,9,10, 11,12,13,14]

#case 2
A = [ ]
B = [1]


my_solution = Solution()
my_solution.merge(A, len(A), B, len(B))

print A







