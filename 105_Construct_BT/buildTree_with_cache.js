const { TreeNode, treeToArray }  = require('../Data_Structure/BTreeNode');

/**
 * Instead of slicing preorder and inorder array each recursion,
 * just pass the desired subarray indices to next recursiion.

 * Time complexity: 
 * It builds every node, so the it take n recursion calls if there is n nodes. 
 * Since we use cache to store inorder array index for each element, we can remove 
 * indexof operation in each recursion. 
 * So the totatl is O(n)
 */
var buildTree = function(preorder, inorder) {
    // build index map for inorder array
    const index_map = {};
    inorder.reduce((acc, cur, index) => {
        acc[cur] = index;  
        return acc
    }, index_map);

	function helper(pre_start, pre_end, in_start, in_end) {

		if ((pre_end - pre_start) <= 0) {
			return null;
		}

		const root = preorder[pre_start];
		const root_indx = index_map[root];
		const rootNode = new TreeNode(root);


		rootNode.left = helper(pre_start + 1, root_indx - in_start + pre_start + 1, in_start, root_indx);
		rootNode.right= helper(root_indx-in_start+pre_start+1, pre_end, root_indx + 1, in_end);
		return rootNode;

	}

	return helper(0, preorder.length , 0, inorder.length );
};


/**
 * Test case
 */

console.log(treeToArray(buildTree([-1], [-1])));
console.log(treeToArray(buildTree([3,9,20,15,7], [9,3,15,20,7])));
console.log(treeToArray(buildTree([12,5,2,9,18,15,13,14,19], [2,5,9,12,13,14,15,18,19])));
