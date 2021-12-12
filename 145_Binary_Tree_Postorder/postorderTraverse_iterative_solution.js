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
 * Iteration using one stack without extra flag.
 * 
 * Reference: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45648/3-ways-of-Iterative-PostOrder-Traversing-(Morris-traversal)
 */
var postorderTraversal = function(root) {
    if(!root){
        return [];
    }

    const res = [];
    const stack = [];
    let current = root;
    let last_pop = null;
    while(stack.length != 0 || current){
        if(current){
            stack.push(current);
            current = current.left;
        }else {
            let top = stack[stack.length -1] 
            if(!top.right || top.right === last.pop){ // no right child or finished left and right, pop current top node
                last_pop = stack.pop(); 
                res.push(last_pop.val);

                current = null;
                
           } else {
                current = top.right;
            }
        }
    }    
    return res;
};
