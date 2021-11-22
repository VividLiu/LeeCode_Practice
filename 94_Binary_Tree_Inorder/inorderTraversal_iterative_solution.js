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

/*
 * Reference: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45559/My-Accepted-code-with-explaination.-Does-anyone-have-a-better-idea 
 *
 * For inorder traversal, we visit a node when pushing its right child in stack. 
 * 
 * Time complexity: O(n), n is # of nodes in the tree.
 * Space complexity: O(h), h is the height of the tee.
 */
var inorderTraversal = function(root) {
    const res = [];
    if(!root){
        return res;
    } 

    const stack = [];
    let currentNode = root;

    while( stack.length > 0 || currentNode){
        if(currentNode){
            stack.push(currentNode);
            currentNode = currentNode.left;
        }else {
            currentNode = stack.pop();
            res.push(currentNode.val);
            currentNode = currentNode.right;
        }
    }
    
    return res; 
};

/**
 * Test
 */

console.log(inorderTraversal(str2tree('')));
console.log(inorderTraversal(str2tree('1(2)(3)')));
console.log(inorderTraversal(str2tree('1()(2(3))')));
