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
var preorderTraversal = function(root) {
    if(!root) {
        return []
    }
    
    const res = [];
    const stack = [root];
    let cur;
    while(stack.length != 0 ) {
        cur = stack.pop();
        res.push(cur.val);
        
        cur.right && stack.push(cur.right);
        cur.left && stack.push(cur.left);
        
    }
    return res;
};
