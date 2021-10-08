const { TreeNode, treeToArray }  = require('../Data_Structure/BTreeNode');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var buildTree = function(preorder, inorder) {
    // sanity check
    if(preorder.length <= 0 || inorder.length <= 0){
        return null;
    }

    // construct inorder array index map
    const index_map = {}
    inorder.reduce((acc, cur, i) => {
        acc[cur] = i;
        return acc;
    }, index_map);
    console.log(index_map);

    let p = 0; 
    let root = preorder[p];
    let node = new TreeNode(preorder[p++]);;
    const stack = [node, [0, index_map[root]], [index_map[root] + 1, preorder.length]];
    let top;

    while(p < preorder.length && stack.length > 0) {
        root = preorder[p];
        top = stack[stack.length -1];

        let s = top[1][0];
        let e = top[1][1];
        let root_index = index_map[root];
        if(s <= root && root < e){ // root is in left 
            node.left = new TreeNode(root);    
            node = node.left;
            stack.push([node, s < root_index? [s, root_index] : null, root_index + 1 < e? [ root_index+1, e]: null);
            top[1] = null;
        } else {
            s = top[2][0];
            e = top[2][1];
            root_index = index_map[root];
            if(s <= root && root < e){ // root is in right 
                node.right= new TreeNode(root);    
                node = node.right;
                stack.push([node, s < root_index? [s, root_index] : null, root_index + 1 < e? [ root_index+1, e]: null);
                top[2] = null;
            }
        }
         
    }
}

/**
 * Test case
 */

console.log(treeToArray(buildTree([-1], [-1])));
console.log(treeToArray(buildTree([3,9,20,15,7], [9,3,15,20,7])));
