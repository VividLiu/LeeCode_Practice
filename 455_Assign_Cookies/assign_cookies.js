/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */

/**
 * Greedy algorithm.
 * Sort both greed factor and cookie array. 
 * Traverse the sorted greed factor array and choose the smallest cookie to satisfy the current child.
 * Time complexisty: sorting g & s => O(N^2 + S^2), traverse => O(max(N,M));
 */
var findContentChildren = function(g, s) {
    const compare = (a, b) => a - b
    g.sort(compare);
    s.sort(compare);
    
    let i = 0; 
    let j = 0;
    let result = 0;
    while( i < g.length && j < s.length) {
        if(g[i] <= s[j]){
            result++;
            i++;
            j++;
        } else {
            j++;
        }
    }
    return result;
};
