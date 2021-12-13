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

/**
 * Iteration using two stacks 
 * 
 * Reference: https://www.geeksforgeeks.org/iterative-postorder-traversal/
 */
var postorderTraversal = function(root) {
    const res = [];
    if(!root) {
        return res;
    }
    const s1 = [root];
    const s2 = [];
    
    let top;
    while(s1.length) {
        top = s1.pop();
        
        s2.push(top);
        top.left && s1.push(top.left);
        top.right && s1.push(top.right);
    }

    //s2 is the reversed order of postorder
    while(s2.length){
        res.push(s2.pop().val);
    }
    return res;
}
 
