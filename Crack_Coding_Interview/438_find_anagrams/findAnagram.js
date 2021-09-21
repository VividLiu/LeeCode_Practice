
const log  = console.log;
const print = console.log;

/*
 * s is long stirng,
 * p is short string,
 * Use a hash map to store the cnt of required letters.
 * Keep a start pointer and current pointer, and slide through the long string.
 */
function findAnagrams(s, p) {

    let start = 0;
    let cur = 0;
    let cnt = p.length;
    let hash = generateHash(p);

    while (start < s.length && cur < s.length) {
        chr= s[cur];
        log('\n i = ' + cur + ' char = ' + chr);

        if (!hash.has(chr)) { //can't be part of anagram
            // reset hash and move start to the one after chr
            log('case1: invalid character');
            hash = generateHash(p);
            cnt = p.length;
            start = cur + 1;
            log('reset start to ' + start + ', cnt = ' + cnt);
        } else if( hash.get(chr) === 0 ) { // # of chr is going to be -1, means we need to remove one chr in the current anagram to make it still valid
            log('case2: extra encountered');
            hash.set(chr, -1);
            let i = start - 1;
            while(i < cur && hash.get(chr) === -1) {
                i++;
                cnt++;
                hash.set(s[i], hash.get(s[i]) + 1);
            }
            cnt--;
            start = i + 1;
            log('set start to ' + start + ', cnt = ' + cnt);
        } else if ( hash.get(chr) > 0) {// still has available chr
            log('case3: valid character');
            hash.set(chr, hash.get(chr) - 1);
            cnt--;

            if (cnt === 0){
                print('found: start = ', start); 
                // advance start by 1
                hash.set(s[start], hash.get(s[start]) + 1);
                start++;
                cnt++; 
            }
            log('set start to ' + start + ', cnt = ' + cnt);
        } else {
            log('Error: this is should never happen');
        }
        log(hash);
        cur++;
    }
}

function generateHash(s) {
    const res = new Map();

    for(let i = 0 ; i < s.length; i++){
        c = s[i];
        if (res.has(c)) {
            res.set(c, res.get(c) + 1);
        } else {
            res.set(c, 1);
        }
    }
    return res;
}

/*
 * Test Case:
 */

// findAnagrams('abab', 'ab');
// findAnagrams('cbaebabacd', 'abc');
