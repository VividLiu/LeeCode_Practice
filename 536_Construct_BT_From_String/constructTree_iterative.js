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
 * Iterative solution
 * When hit '(', create new tree node using the following number and push it into stack. Note the number could be multiple digits and negative. 
 * When hit ')', pop the top node and attach it to the child of new top node.
 * To determine it goes to left child or right child: 
 * The question comes with the constraint that it always construts left child first, which means there is no siution that right child exists while left child is null.
 * With this constraint, we can simply check if left child is null or not null, to determine the new node goes to left or right. 
 * Without this constraint, we can in stack tuple instead of just node: (node, isLeft), 
 * and use the isLeft flag to determine if it left child is set or not.  
 *
 * Time complexity: O(n), n is the length of input string
 * Space complexity: O(m), m is the heigth of the tree. m <= n.
 */
function str2tree(input) {
    if (!input) {
        return null;
    }

    // push root node
    const [val, j] = extractNumber(input, 0);
    const stack = [];
    const root = new TreeNode(val);
    stack.push(root);    

    let i = j; 
    let child;
    let parent;
    while (i < input.length) {
        console.log('\n i = ', i);
        if(input[i] === '(') {
            const [val, j] = extractNumber(input, i+1);
            stack.push(new TreeNode(val));    
            // console.log('hit (. extract number ', val);
            // console.log('move pointer to : ',j);
            i = j; 
        }else if (input[i] === ')'){
            if(stack.length < 2){
                console.log('stack is wrong');
            } 
            child = stack.pop();    
            parent = stack[stack.length -1 ] 
            !parent.left? parent.left = child: parent.right = child;
            // console.log('hit ).  ', );
            // console.log('move pointer to : ',i+1);
            i++;
        }else {
            console.log('something is wrong');
        }
        // console.log('stack: ', stack);
    }
    return root;
}

/**
 * Utility function to extra first node value from input[start: end] substring.
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

/*
console.log(extractNumber('', 0));
console.log(extractNumber('-123)', 0));
console.log(extractNumber('-1', 0));
console.log(extractNumber('123', 0));
console.log(extractNumber('-123(2)', 0));
*/

console.log(treeToArray(str2tree('')));
console.log(treeToArray(str2tree('-1')));
console.log(treeToArray(str2tree('3(9)(20(5)(7))')));
console.log(treeToArray(str2tree('12(5(2)(9))(18(15(13()(14)))(19))')));
/*
*/
