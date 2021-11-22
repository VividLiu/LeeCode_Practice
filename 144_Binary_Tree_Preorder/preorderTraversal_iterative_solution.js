/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


/**
 * Reference: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45559/My-Accepted-code-with-explaination.-Does-anyone-have-a-better-idea
 * https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization
 * For preorder traversal, we visit a node when pushing it in stack.
 */

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    if(!root) {
        return []
    }
    
    const res = [];
    const stack = [];
    let current = root;
    while(stack.length != 0 || current) {
        if(current){
            res.push(current.val);
            stack.push(current);
            current = current.left;
        }else {
            current = stack.pop();
            current = current.right;
        }    
    }
    return res;
};
