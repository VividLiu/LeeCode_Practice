const { str2tree } = require('../536_Construct_BT_From_String/constructTree_original.js');

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


/*
 * Post-order traverse the tree with iterative method, 
 * and store each node's height in an extra map. 
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    if(!root){
        return true
    }

    const height_map = new Map();
    const stack = [];
    let cur = root;
    let last = null;
    let top = null;

    while(cur || stack.length){
        if(cur){
            stack.push(cur);
            cur = cur.left;
        }else {
            top = stack[stack.length-1];
            if(top.right==null){
                last = stack.pop();
                cur = null; 
                if(!getNodeHeight(last, height_map)){
                    return false;
                }
            }else if(top.right == last){
                last = stack.pop();
                cur = null;
                if(!getNodeHeight(last, height_map)){
                    return false;
                }
            }else {
                cur = top.right;
            }
        }    
    }
    return true;
};

var getNodeHeight = function(node, height_map) {
    if(!node){
        return 0;
    }

    const left_child_height = node.left? height_map.get(node.left) : 0;
    const right_child_height = node.right? height_map.get(node.right) : 0;
    const h = Math.max(left_child_height, right_child_height) + 1;
    height_map.set(node, h);
    if (Math.abs(left_child_height - right_child_height) > 1) {
        return false; 
    }
    return true;
}

// console.log(isBalanced(str2tree('1')));
 console.log(isBalanced(str2tree('1(2(4(6))(5))(3)')));
