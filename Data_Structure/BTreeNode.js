/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

class TreeNode {

    constructor(val, left, right) {
        this.val = val || 0;
        // this.left = (left=== undefined ? null: left);
        this.left = left || null; 
        this.right = right || null;

    }

}

// convert TreeNode into array representation
function treeToArray(root){
        const res = [];
        const stack = [root];

        function bfs() {
            while(stack && stack.length) {
                const top = stack.shift();
                if (top) {
                    res.push(top.val); 
                    stack.push(top.left)
                    stack.push(top.right)
                } else {
                    res.push(null);
                }
            }
        }

        bfs();

        let i = res.length - 1;
        while(i && !res[i]) {
            res.pop()
            i--
        }
        return res;
}

/*
 * Test Case
 */
// const t = new TreeNode(3, new TreeNode(2, null, new TreeNode(1)), new TreeNode(4));

module.exports = {
    TreeNode: TreeNode,
    treeToArray: treeToArray
}
