/**
 * permuations_2 generate permutataion of s recursively.
 * The permutation of s consist of s[i] concatenated with each permutation of substring s[0,i] + s[i+1, 0], i = 0...n; 
 * For example:
 * perms('abc') 
 * => a + each in perms('bc'), b + each in perms('ac'), c + each in perms('ab')
 * => a + ['bc', 'cb'], b + ['ac', 'ca'], c + ['ab', 'ba']
 */
function permutations(remain) {
    if(remain.length === 1) {
        return [remain]
    }
    const res = [];
    for(let i = 0; i < remain.length; i++ ) {
        const postfix = permutations(remain.slice(0, i)+ remain.slice(i+1));
        postfix.forEach((item) => {
            res.push(remain[i] + item);
        });
    }
    return res;
}


/**
 * Test Case
 */

console.log(permutations(''));
console.log(permutations('a'));
console.log(permutations('abc'));
console.log(permutations('abcd'));

