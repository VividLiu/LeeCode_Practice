const { TreeNode, treeToArray }  = require('../Data_Structure/BTreeNode');

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/**
 * Recursive solution. 
 * When hit a open parathenese, it means the start of a new subtree, construct a new node. 
 * The recursive function will also return the end of the current tree, so we don't need to have another iteration to search for matching pair.
 * When hit a close parenthese, it means the finish of a current node, we need to return the node and correct index. 
 * Time complexity: O(n)
 */
function str2tree(input) {
    const treeBuilder = (start) => {
        if(start >= input.length){
            return [ null, 0];
        }

        let rootVal;
        let next; // next processing character

        // always start with number
        [rootVal, next] = extractNumber(input, start);
        const rootNode = rootVal !== NaN? new TreeNode(rootVal) : null;

        if(!rootNode) {
            console.log('Got invalid root value start at:', start);
        }
    
        // current root has left subtree
        if(next < input.length && input[next] === '(') {
            console.log(`node ${rootVal} has left subtree`);
            // new next will pointing to end index of the left subtree + 1
            [rootNode.left, next] = treeBuilder(next + 1);
            
            // current root has right substree
            if(next < input.length && input[next] === '(') {
                console.log(`node ${rootVal} has right subtree`);
                [rootNode.right, next] = treeBuilder(next +1);
            }
        }

        // When hit a closing parathense, it means the construction of a node is finished.
        // case 1: 
        // If next is the value returned from extractNumber(input, start),
        // it means the current root has no left or right subtree.
        // The construction of current root is finisehd, and we can return the node and next index to process
        // Example: '1(2)(4)' and current node is 4, return [node(4), ]
        // Example: '1(2)(4)' and current node is 2, return [node(2), ]
        // case 2: 
        // If next is the value returned from [node.left, next] = treeBulder(next+1),
        // it means the current root has left subtree but no right subtree.
        // Example: '1(2)' and current node is 1, return [node(1), ]
        // Example: '0(1(2))' and current node is `, return [node(1), ]
        // case 3: 
        // If next is the value returned from [node.right, next] = treeBulder(next + 1),
        // it means the current root has both left subtree and right subtree,   
        // and it has finished construct both. We will go back to process the parent of current root node.
        // Example: '1(2)(4)' and current node is 1, return [node(1), ]
        // Example: '0(1(2)(4))(5)' and current node is 1 return [node(1), ], next to process 5.
        if(next >= input.length || input[next] === ')' ) {
            return [rootNode, next + 1];
        }

        // reaching end of string
        return [rootNode, Number.MAX];
   }        
    return treeBuilder(0)[0];
}

/**
 * Utility function to extract first digit value from input[start: end] substring 
 * 
 * Return a tuple of parsed value and value end index.
 * Example: func('2(3)(1)', 0) => [2, 1], 1 is the end index of value '2'.
 *          func('2(3)(1)', 2) => [3, 3], 3 is the end index of value '3'
 * The end index will be index of a '(' or ')' or end of the string. 
 */
function extractNumber(input, start) {
    if(start >= input.length){
        return [ NaN, -1]
    }

    let isNeg = 1; 
    let number = 0; 
    let i;
    for(i = start; i < input.length; i++) {
        if(input[i] === '-'){
            isNeg = -1;
        }else if(input[i] === '(' || input[i] === ')'){
            break;
        }else {
            number = number * 10 + Number(input[i]); 
        }
    }
    return [ isNeg * number, i]
}

/**
 * Test case
 */
console.log(treeToArray(str2tree('')));
console.log(treeToArray(str2tree('-1')));
console.log(treeToArray(str2tree('-1(2)')));
console.log(treeToArray(str2tree('-1(-2)')));
console.log(treeToArray(str2tree('-1(2)(3)')));
console.log(treeToArray(str2tree('-1(2)(-3)')));
console.log(treeToArray(str2tree('3(9)(20(5)(7))')));
console.log(treeToArray(str2tree('12(5(2)(9))')));
console.log(treeToArray(str2tree('12(5(2)(9))(18(15(13()(14)))(19))')));
