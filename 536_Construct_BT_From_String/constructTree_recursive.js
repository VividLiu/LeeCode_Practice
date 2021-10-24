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
 * The left subtree is beween the first pair of matching parenthese if it exists. 
 * The right subtree is between the second pair of matching parenthese if it exists.
 * 
 * For example: '-30(2(9)(6))(1)'
 * -30 is root node, 
 * left subtree of -30 is defined in '(2(9)(6))',
 * right subtree of -30 is defined in '(1)'
 * 
 * root = new TreeNode(30)
 * root.left = recursion('2(9)(6)')
 * root.right = recursion('1') 
 * 
 * Time complexity: O(n^2)
 * If n is the length of the string, m is the number of nodes, 
 * the algorithm requires O(m) recursion (m < n). 
 * Each recursion round, it traverse through the substring. 
 * Because each recursion rount, it construct one root node, so the length of substring is reduced by one node. 
 * Maximally, O(n) + O(n-c) + O(n-2c) ... O(c) => O(n^2)
 * c is constant, average node length in string.
 * 
 */
function str2tree(input) {
    const treeBuilder = (start, end) => {
        // console.log(`\nstart = ${start}, end = ${end}`);
        if(start >= end){
            return null;
        }

        const [nodeVal, valEnd] = extractNumber(input, start);
        
        // console.log(`nodeVal = ${nodeVal}, valEnd = ${valEnd}`);
        const node = new TreeNode(nodeVal);

        // find the first matching pair of parenthese,
        // which represents the left subtree of current node
        let cnt = 0;
        let i = valEnd;
        for(; i < end; i++){
            if(input[i] === '(') {
                cnt++;
            } else if (input[i] === ')') {
                cnt--;
            }    
            if(!cnt) {
                i++;
                break;
            }
        }   
        node.left = treeBuilder(valEnd + 1, i);
        node.right = treeBuilder(i+1, end-1); 

        return node;
    }        
    return treeBuilder(0, input.length);
        
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
