const { TreeNode, treeToArray } = require('../Data_Structure/BTreeNode');
const { str2tree } = require('../536_Construct_BT_From_String/constructTree_original.js');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    
    const res = []
    const helper = (node) => {
        node.left && helper(node.left);
        res.push(node.val);    
        node.right && helper(node.right);
    }

    root && helper(root);
    return res;
};

/**
 * Test
 */

console.log(inorderTraversal(str2tree('')));
console.log(inorderTraversal(str2tree('1(2)(3)')));
console.log(inorderTraversal(str2tree('1()(2(3))')));
