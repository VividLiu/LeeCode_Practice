/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


/*
 * DFS 
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    const helper = (node) => {
        if(!node) {
            return [0, true];
        }

        const [left_h, left_balanced] = helper(node.left);
        const [right_h, right_balanced] = helper(node.right);

        return [Math.max(left_h+1, right_h+1), left_balanced && right_balanced && Math.abs(left_h - right_h) < 2];
    }

    return helper(root)[1];
};
