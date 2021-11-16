const { str2tree } = require('../536_Construct_BT_From_String/constructTree_original.js');

/*
 * Traverse the tree in any order(iteratively or recursively)
 * and invert direct child of each node
 */
var invertTree = function(root) {
    const stack = [];
    let current = root;
    let swap;
    
    while(stack.length !== 0 || current) {
        if(current){
            swap = current.left;
            current.left = current.right;
            current.right = swap;
            
            stack.push(current);
            current = current.left
        }else {
            current = stack.pop();
            current = current.right;
        }  
    }
    
    return root;
};

/**
 * Test
 */
console.log(invertTree(str2tree('4(2(1)(3))(7(6)(9))')));

