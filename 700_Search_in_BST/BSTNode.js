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

        // console.log('constructor this: ', this);
        this.flatten = this.flatten.bind(this);
        this.array = this.flatten();
    }

    // convert TreeNode into array representation
    flatten() {
        const res = [];
        const stack = [this];

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

    // define customer console.log behavior 
    print() {
        console.log(this.array);
    }
}

const t = new TreeNode(3, new TreeNode(2, null, new TreeNode(1)), new TreeNode(4));
// const t = new TreeNode(3, new TreeNode(2), new TreeNode(4));

t.print();
