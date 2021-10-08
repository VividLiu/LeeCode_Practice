const { TreeNode, treeToArray }  = require('../Data_Structure/BTreeNode');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Due to the nature of preorder traversing, we know that preorder[0] is root node. 
 * We then find the index of pre[0] in inorder array, assuming x. 
 * Then inorder[0...x-1] is the left subtree of root, inorder[x+1...n] is the right 
 * subtree of root node, base of indorder traversing nature. 
 * Do the step recursively, we can bulid the tree. 
 * 
 * preorder traversal provides us with the placement of the root
 * inorder traversal provides us with the placement of the left and right children
 * 
 * Time complexity: 
 * It builds every node, so the it take n recursion calls if there is n nodes. 
 * In each iteration, it takes one indexOf, 4 slice operation, both of them are O(n).
 * So the totatl is O(n^5)
 */

var buildTree = function(preorder, inorder) {
        if(preorder.length != inorder.length){
                console.log('something is wrong');
        }
        if (!preorder.length) {
                return null;
        }

        const root = preorder[0];
        const root_indx = inorder.indexOf(root);
        const rootNode = new TreeNode(root);

        rootNode.left = buildTree(preorder.slice(1, root_indx+1), inorder.slice(0, root_indx));
        rootNode.right= buildTree(preorder.slice(root_indx+1,), inorder.slice(root_indx + 1));
        return rootNode;
};

/**
 * Test case
 */

console.log(treeToArray(buildTree([-1], [-1])));
console.log(treeToArray(buildTree([3,9,20,15,7], [9,3,15,20,7])));
console.log(treeToArray(buildTree([12,5,2,9,18,15,13,14,19], [2,5,9,12,13,14,15,18,19])));
