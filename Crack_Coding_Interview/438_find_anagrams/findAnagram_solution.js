/**
 * Sliding window:
 * Instead of separate the case when hitting the character that doesn't exsit in p,
 * and the case when hitting extra character,
 * combine these two cases as they follow the same logic:
 * hash[char] becomes -1, and need to advance start pointer until the hahs[char] becomes 0 again.
 *
 * Reference: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/639309/Java-Sliding-Window-Clear-explanation-Easy-to-understand-Clean-and-Concise
 */
function findAnagrams(s, p) {
    const hash = Array(26).fill(0);
    const ascii_a = 'a'.charCodeAt(0);
    const res = [];
    let cnt = p.length;
    let chr;

    // create the cnt hash for p string
    for(let i = 0; i < p.length; i++) {
        hash[p.charCodeAt(i) - ascii_a]++;
    }     
    
    for(let start = 0, end = 0; end < s.length; end++) {
        ascii_chr = s.charCodeAt(end) - ascii_a;
        hash[ascii_chr]--;
        cnt--;

        if (hash[ascii_chr] === 0) {
            if(!cnt) { //found valid anagram
                res.push(start);
                //advance start by 1
                hash[s.charCodeAt(start) - ascii_a]++;
                start++;
                cnt++;
            } 
             
        } else if(hash[ascii_chr] < 0 ) { // current char makes the anagram invalid. It either doesn't exist in p or we already include enough of the char in current anagram. Need to move the start pointer to make the anagram valid again. 
            while(hash[ascii_chr] < 0) {
                hash[s.charCodeAt(start) - ascii_a]++;
                start++;
                cnt++;
            } 
        } 
    }

    return res;
}

/**
 * Test Case
 **/
console.log(findAnagrams('aab', 'ab'));
console.log(findAnagrams('abab', 'ab'));
console.log(findAnagrams('cbaebabacd', 'abc'));

