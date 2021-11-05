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
 * @return {boolean}
 */

/*
 * Reference: https://leetcode.com/problems/validate-binary-search-tree/solution
 */
var isValidBST = function(root) {
    const helper = (node, min, max) => {
        let isValid;
        isValid = node.left? (node.left.val < node.val && node.left.val > min && helper(node.left, min, node.val)) : true;
        isValid = node.right? (node.right.val > node.val && node.right.val < max && helper(node.right, node.val, max)) && isValid: isValid;
        return isValid;
    }
    if(!root){
        return true;
    }
    return helper(root, -Number.MAX_VALUE, Number.MAX_VALUE);
 };

/**
 * Test
 */
console.log(isValidBST(str2tree('0')));
console.log(isValidBST(str2tree('')));
console.log(isValidBST(str2tree('1')));
console.log(isValidBST(str2tree('2(1)(3)')));

console.log(isValidBST(str2tree('1(2)(3)')));
console.log(isValidBST(str2tree('3(2)(1)')));
console.log(isValidBST(str2tree('5(4)(6(3)(7))')));
