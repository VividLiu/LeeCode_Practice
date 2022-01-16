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
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    const newNode = new TreeNode(val, null, null);
    if(!root){
        return newNode;  
    }    

    const par = null;
    const cur = root;

    while(cur){
        par = cur;
        cur = val > cur.val ? cur.right : cur.left;
    }

    if(val > par.val && !par.right) {
        par.right = newNode;
    }else if(val < par.val && !par.left){
        par.left = newNode;
    }else {
        console.log('something is wrong');
    }

    return root;
};
