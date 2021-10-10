const { TreeNode, treeToArray }  = require('../Data_Structure/BTreeNode');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Put 
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


    const stack = [];

    // put root node into stack
    let p = 0; 
    let root = preorder[p];
    let root_index = index_map[root];
    let tree = new TreeNode(preorder[p++]);;
    stack.push({
        node: tree, 
        ls: 0 < root_index ? 0: Number.MAX_VALUE,
        le: 0 < root_index ? root_index: Number.MIN_VALUE,
        rs: root_index + 1 < preorder.length ? root_index+1 : Number.MAX_VALUE,
        re: root_index + 1 < preorder.length ? preorder.length : Number.MIN_VALUE,
    });


    let top; 
    let lflag = true;
    let rflag = true;

    while(p < preorder.length && stack.length > 0) {
        root = preorder[p++]; 
        root_index = index_map[root]; 
        top = stack[stack.length -1]; 

        const {node, ls, le, rs, re} = top;

        if(ls === Number.MAX_VALUE && rs === Number.MAX_VALUE){ // already processed both left subtree and right subtree.
            stack.pop();
            p--
        } else if(ls <= root_index && root_index < le) { // current node is in the left subtree of top 
            node.left = new TreeNode(root);    
            lflag = ls < root_index;
            rflag = root_index + 1 < le;

            // if both lflag and rflag are false, means the current node is a leaf node, no need to push into stack
            if (lflag || rflag) { 
                stack.push({
                    node: node.left,
                    ls: lflag ? ls : Number.MAX_VALUE,
                    le: lflag ? root_index : Number.MIN_VALUE,
                    rs: rflag ? root_index+1 : Number.MAX_VALUE,
                    re: rflag ? le : Number.MIN_VALUE,
                });
            }

            // processing left subtree of top node, invalidate the it so it can be poped when comes back
            top.ls = Number.MAX_VALUE; 
            top.le = Number.MIN_VALUE;

        } else if(rs <= root_index && root_index < re) {
            node.right= new TreeNode(root);    

            lflag = rs < root_index;
            rflag = root_index+1 < re;

            // if both lflag and rflag are false, means the current node is a leaf node, no need to push into stack
            if (lflag || rflag) { 
                stack.push({
                    node: node.right,
                    ls: lflag ? rs : Number.MAX_VALUE,
                    le: lflag ? root_index : Number.MIN_VALUE,
                    rs: rflag ? root_index+1 : Number.MAX_VALUE,
                    re: rflag ? re : Number.MIN_VALUE,
                });
            }

            // processing right subtree of top node, invalidate the it so it can be poped when comes back
            top.rs = Number.MAX_VALUE; 
            top.re = Number.MIN_VALUE;
        } else {
            console.log('something is wrong');
        }
    }
    return tree;
}

/**
 * Test case
 */

// console.log(treeToArray(buildTree([-1], [-1])));
//console.log(treeToArray(buildTree([2, 1, 9], [1, 2, 9])));
console.log(treeToArray(buildTree([3,9,20,15,7], [9,3,15,20,7])));
// console.log(treeToArray(buildTree([12,5,2,9,18,15,13,14,19], [2,5,9,12,13,14,15,18,19])));
