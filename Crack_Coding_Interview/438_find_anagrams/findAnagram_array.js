const log = () => {};
const print = console.log;
/**
*
*/
function findAnagrams_array(s, p) {

    let start = 0;
    let cur = 0;
    let cnt = p.length;
    const hash = Array(26).fill(-2);
    generateArray(hash, p);
    const ascii_a = 'a'.charCodeAt(0);
    let arr_idx;

    while (start < s.length && cur < s.length) {
        chr= s[cur];
        arr_idx = s.charCodeAt(cur) - ascii_a;
        log('\n i = ' + cur + ' char = ' + chr);

        if (hash[arr_idx] === -1) { //can't be part of anagram
            // reset hash and move start to the one after chr
            log('case1: invalid character');
            generateArray(hash, p);
            cnt = p.length;
            start = cur + 1;
            log('reset start to ' + start + ', cnt = ' + cnt);
        } else if( hash[arr_idx]  === 0 ) { // # of chr is going to be -1, means we need to remove one chr in the current anagram to make it still valid
            log('case2: extra encountered');
            hash[arr_idx] = -1;
            cnt--;

            let i = start - 1;
            while(i < cur && hash[arr_idx] === -1) {
                i++;
                cnt++;
                hash[s.charCodeAt(i) - ascii_a]++;
            }
            start = i + 1;
            log('set start to ' + start + ', cnt = ' + cnt);
        } else if (hash[arr_idx] > 0) {// still has available chr
            log('case3: valid character');
            hash[arr_idx] --;
            cnt--;

            if (cnt === 0){
                print('found: start = ', start); 
                // advance start by 1
                hash[s.charCodeAt(start) - ascii_a]++;
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


function generateArray(arr, p) {
    if (arr.length < 26) {
        log('Cnt array needs to have 26 length');
    }
    for(let i = 0; i < 26; i++){
        arr[i] = -1;
    }
    const ascii_a = 'a'.charCodeAt(0);
    p.split('').map((_, i) => {
        const idx = p.charCodeAt(i) - ascii_a;
        arr[idx] = (arr[idx] === -1 ?  1 : arr[idx] + 1) ;
    })
}

/**
 * Test Case
 **/
findAnagrams_array('abab', 'ab');
findAnagrams_array('cbaebabacd', 'abc');
