const { str2tree } = require('../536_Construct_BT_From_String/constructTree_original.js');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
 * Base on property of bst inorder travserse.
 * If it is a bst tree, the inorder traverse should generate the sequence in sorted order.
 * The solution is inorder traversing the bst tree, and compare the processed node with a precessor. 
 * Whevener pop a node from stack, the node is processed in inorder traversing sequence, 
 * hence the node value should be updated to precessor.
 * Time complexity: O(n)
 * Space complexity: O(n)
 * Reference: https://leetcode.com/problems/validate-binary-search-tree/solution/
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    if(!root){
        return true;
    }

    let current = root;
    let stack = [];
    let precessor = -Number.MAX_VALUE;
    let top;

    while(stack.length > 0 || current) {
        if(current){
            top = stack.length ? stack[stack.length-1].val : Number.MAX_VALUE;
            if(!(current.val < top && current.val > precessor)) {
                return false; 
}

            stack.push(current);
            current = current.left
        }else {
            current = stack.pop();    
            precessor = current.val;
            current = current.right
        }
    }
    return true;
 };

/**
 * Test
 */
console.log(isValidBST(str2tree('0')));
/*
console.log(isValidBST(str2tree('')));
console.log(isValidBST(str2tree('1')));
console.log(isValidBST(str2tree('2(1)(3)')));

console.log(isValidBST(str2tree('1(2)(3)')));
console.log(isValidBST(str2tree('3(2)(1)')));
console.log(isValidBST(str2tree('5(4)(6(3)(7))')));
*/
