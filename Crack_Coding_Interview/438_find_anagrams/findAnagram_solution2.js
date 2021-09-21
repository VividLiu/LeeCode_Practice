/**
 * Maintain a window of p length in s string, two hash of character frequency in p and in s respectively (hash_p, hash_s).
 * Keep moving the window, and compare the equality of hash_p and hash_s every step.
 * Because the fixed number of charaters, maximumly 26, the comparision at each step is constant time.
 * The algorithm is still linear.
 * 
 * Reference: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/175381/Sliding-Window-Logical-Thinking
 */
function findAnagrams(s, p) {
    const hash_p = new Map();
    const hash_s = new Map();
    const res = [];
    let start = 0;

    // populate frequency map for p.
    for(let i = 0; i < p.length; i++) {
        hash_p.set( p[i], hash_p.has(p[i]) ? hash_p.get(p[i]) + 1 : 1);
    }

    //slide
    for(let i = 0; i < s.length; i++) {
        // populate frequence map for s.
        if ( i < p.length - 1) {
            hash_s.set( s[i], hash_s.has(s[i]) ? hash_s.get(s[i]) + 1 : 1);
           continue; 
        }

        hash_s.set( s[i], hash_s.has(s[i]) ? hash_s.get(s[i]) + 1 : 1);

        start = i - p.length + 1;
        if (compareMaps(hash_s, hash_p)) {
            res.push(start); 
        }

        //advance start
        if (hash_s.get(s[start]) === 1) {
            
            // remove the counter so the it doesn't become -1, which impact compareMaps accuracy.
            hash_s.delete(s[start]);
        } else {
            hash_s.set(s[start], hash_s.get(s[start]) - 1);
        }
    }

    return res;

}


function compareMaps(map1, map2) {
    var testVal;
    if (map1.size !== map2.size) {
        return false;
    }
    for (var [key, val] of map1) {
        testVal = map2.get(key);
        // in cases of an undefined value, make sure the key
        // actually exists on the object so there are no false positives
        if (testVal !== val || (testVal === undefined && !map2.has(key))) {
            return false;
        }
    }
    return true;
}

/*
 * Test Case:
 */

console.log(findAnagrams('abab', 'ab'));
console.log(findAnagrams('cbaebabacd', 'abc'));
