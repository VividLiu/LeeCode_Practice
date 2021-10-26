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

function str2tree(input) {
    const treeBuilder = (start, end) => {
        if(start >= end){
            return null;
        }

        // console.log('\n');
        // find root node value
        const ls = input.indexOf('(', start) === -1? input.length : input.indexOf('(', start);
        let rootVal;
        let rootNode;

        if( ls > 0) {
            rootVal = parseInt(input.slice(start, ls));
            if(rootVal == NaN){
                return null;
            }
            rootNode = new TreeNode(rootVal);
        }else {
            console.log(`Invalid input string ${input}`);
            return;
        }

        // console.log('rootnode: ', rootNode);

        let le = 0;
        let cnt = 0;
        //find matching paranthese for left sub tree
        for(le = ls; le < end; le ++ ){
            if(input[le] === '(') {
                cnt++;
            }    
            if(input[le] === ')') {
                cnt--;
            }    
            if(!cnt){
                break;
            }
        }

        //find right parathenese for right sub tree
        let rs = le + 1;
        let re;
        cnt = 0;
        for(re = rs; re < end; re++){
            if(input[re] === '(') {
                cnt++;
            }    
            if(input[re] === ')') {
                cnt--;
            }    
            if(!cnt){
                break;
            }
        } 

        // console.log(`ls = ${ls}, le = ${le}`);
        // console.log(`rs = ${rs}, re = ${re}`);

        rootNode.left = ls < le? treeBuilder(ls + 1, le ): null;
        rootNode.right = rs < re? treeBuilder(rs + 1, re ): null;

        return rootNode;
    }

    return treeBuilder(0, input.length);
}

/**
 * Test case
 */
/*
console.log(treeToArray(str2tree('-1')));
console.log(treeToArray(str2tree('3(9)(20(5)(7))')));
console.log(treeToArray(str2tree('12(5(2)(9))(18(15(13()(14)))(19))')));
*/

module.exports = {
    str2tree
}
