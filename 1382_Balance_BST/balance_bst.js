const { str2tree } = require('../536_Construct_BT_From_String/constructTree_original.js');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Traverse the tree using inorder traversal to get a sorted array.
 * Rebuild the tree using the sorted array, pick the median element for root recursively
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var balanceBST = function(root) {
    const sortedArray = inOrderTraverse(root);
    console.log(sortedArray);
    const tree = buildBalanceBST(sortedArray); 

    return tree;
};

var buildBalanceBST = function(arr) {

    const helper = (startIndex, endIndex) => {
        if(endIndex <= startIndex){
            return null;
        }

        const median = Math.floor((endIndex - startIndex) / 2) + startIndex;

        const root = arr[median];
        root.left = helper(startIndex, median);
        root.right = helper(median + 1, endIndex);
        return root;
    }

    return helper(0, (arr && arr.length) ? arr.length : 0);
}

var inOrderTraverse = function(root){
    if(!root){
        return [];
    }

    let cur = root;
    let stack = [];
    let res = [];
    let top = null;

    while(cur || stack.length) {
        if(cur){
            stack.push(cur);
            cur = cur.left;
        }else {
            top = stack.pop(); 
            res.push(top);
            cur = top.right;
        }
    }
    return res;
}

/*
 * Testing
 */
//console.log(balanceBST(str2tree('1')));
 console.log(balanceBST(str2tree('5(4(2(1))(3))(7(6)(8))')));
