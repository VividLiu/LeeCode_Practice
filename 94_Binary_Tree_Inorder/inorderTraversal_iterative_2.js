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
 * Put (node, isLeftDone) tuple into stack,
 * if isLeftDone flag is set, it means left subtree of node is processed,
 * we can pop node and push right child into stack,
 * if isLeftDoen flag is not set, it means left sutree of node is not processed,
 * then we push left child into stack and set the flag.
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
