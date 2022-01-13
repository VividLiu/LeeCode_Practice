/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


/*
 * wrong answer: 
 * Breadth first search in tree.
 * When a node reaches leaf, record the height h, 
 * continue the breadth first in other node, but the height of other node can't exceed h + 1; 
 * 
 * Example: 
 *        1
 *      /   \
 *     2     3
 *    / \   / 
 *   4   5 6   
 *  /
 * 8
 * 
 * This tree is a balanced tree. The height of left tree of root is 1,
 * the height of right tree of root is 2.
 * 
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    if(!root){return true;}

    const queue = [[root, 1]];        
    let maxHeight = 0;
    
    let current;
    let h;
    let tuple;
    while(queue.length != 0) {
        tuple = queue.shift(); 
        current = tuple[0];
        h = tuple[1];

        if(maxHeight && h > maxHeight + 1){
            return false;
        }
        
        current.left && queue.push([current.left, h+1]);
        current.right && queue.push([current.right, h+1]);
        if(!current.left && !current.right && !maxHeight){
            maxHeight = h;        
        }
    }

    return true;
};
