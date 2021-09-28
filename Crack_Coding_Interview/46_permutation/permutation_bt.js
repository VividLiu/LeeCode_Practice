/**
 * Give a string s with length n, the output will be array of n!.
 * Use backtracking algorithm, each time choose a character from 
 * remaining character list and append it to the generated string.
 * Remove the chosen character from remaining list.
 * 
 *                  ___
 *          /       |       \
 *        a__       b__     c__ 
 *      /  \        / \      / \
 *   ab_   ac_    ba_  bc_  ca_ cb_
 *    |     |     |     |   |    |
 *   abc   acb   bac   bca  cab  cba
 */

function permutations(s) {
    const res = [];

    function helper(prefix, remain) {
        if(remain === '') {
            res.push(prefix)
        }    

        // Iterate through remaining character,
        // pick one and append it to prefix
        for(let i = 0; i < remain.length; i++) {
            helper(prefix + remain[i], remain.slice(0, i) + remain.slice(i+1))
        }
    }

    helper('', s);

    return res;
}



/**
 * Test Case
 */

console.log(permutations(''));
console.log(permutations('a'));
console.log(permutations('abc'));
console.log(permutations('abcd'));

