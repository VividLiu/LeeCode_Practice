/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Use a flag to indiciate if the node is visited or not.
 * When the node is first pushed in stack, the isVisited flag is set to false, 
 * indicating that its left and right subtrees have not been finished processing.
 * If the flag is set, means the left and right subtrees have finished processing,
 * the root node can be poped.
 * 
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    if(!root) {
        return [];
    }
    
    const res = [];
    //in stack element [node, isVisited]
    const stack = [[root, false]];
    
    while(stack.length != 0) {
        const [node, isVisited] = stack[stack.length - 1];
        if(isVisited) {
            res.push(node.val);
            stack.pop();
        } else {
            stack[stack.length - 1][1] = true;
            node.right && stack.push([node.right, false]);
            node.left && stack.push([node.left, false]);
        }
    }
    return res;
    
};
