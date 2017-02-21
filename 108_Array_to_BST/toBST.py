#definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums) 
    
    def helper(self, nums):
        """
        : type nums: List[int]    
        : rtype: TreeNode
        """
        tree = TreeNode()

        #threshold case
        if not nums:
            return None
        #if len(nums) == 1:
        #    tree.val = nums[0]
        #    tree.left = None
        #    tree.right = None
        #if len(nums) == 2:
        #    tree.val = nums[1]
        #    tree.left = self.helper(nums[0:1])
        #    tree.right = None

        #recursively construct tree
        #pivot = Math.floor(len(nums)/2)
        #pivot = len(nums) // 2 # "//" operator is integer division, which equal to floor(x/y)
        pivot = (len(nums) - 1) // 2 #Use this formula instead of len(nums)//2 to meet LeeCode judging requirement 
        tree.val = nums[pivot]
        tree.left = self.helper(nums[:pivot])
        tree.right = self.helper(nums[pivot+1:])  
    
        return tree





