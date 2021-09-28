/**
 * dfs: Keep an array of visited. 
 * If not visited, set visited[i] to true and jadd the current character in existing perm, and go deep.
 * when it comes back to the same node back from recursion, remove the character and reset visited[i] to false.
 * Time complexity: O(n^n)
 * Reference: https://leetcode.com/problems/permutations/discuss/685868/DFSbacktracking-PythonJavaJavascript-PICTURE
 */
function permutations(s) {
    const res = [];
    function dfs(perm, visited){
        if(perm.length === s.length){
            res.push(perm);
        }
        for(let i = 0 ; i < visited.length; i++) {
            if(!visited[i]){
                visited[i] = 1;
                dfs(perm + s[i], visited);
                visited[i] = 0;
            }
        }
    }

    if(!s) {
        return res;
    }

    dfs('', Array(s.length).fill(0));

    return res;
}

/**
 * Test Case
 */

console.log(permutations(''));
console.log(permutations('a'));
console.log(permutations('abc'));
console.log(permutations('abcd'));

