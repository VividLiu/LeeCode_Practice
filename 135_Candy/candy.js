/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    /**
     * find the index where decreasing stops
     */
    const lookDecAhead = (s) => {
        let i = s;
        let j = i + 1; 
        while(j < ratings.length && ratings[i] > ratings[j])        {
            i++;
            j++;
        }
        return i;
    }
    
    /*
     * find the index where increasing stops
     */
    const lookIncAhead = (s) => {
        let i = s;
        let j = i + 1; 
         while(j < ratings.length && ratings[i] < ratings[j]){
            i++;
            j++;
        }
        return i;
    }
    
    let i = 0;
    let cnt = 0;
    let incStop = 0;
    let decStop = 0;
    let preInc = false;
    let preEnd = -1;
    while(i < ratings.length){
        if( i === ratings.length -1){
            if(ratings[i] === ratings[i-1]){
                cnt++;
            }else if(ratings[i] > ratings[i-1]){
                cnt += 2;
            }else if(ratings[i] < ratings[i-1]){
                cnt++;
            }
            break;
        }
        incStop = lookIncAhead(i);
        decStop = lookDecAhead(i);

        /*
        console.log('i: ', i);
        console.log('inc stop at : ', incStop);
        console.log('dec stop at: ', decStop);
        */

        if((i == incStop) && (decStop > i)){// decreasing case
            if(preInc && (ratings[i] !== ratings[i-1]) && (decStop - i + 2) > preEnd) {
                // console.log('preInc true at i = ', i);
                cnt += sumToN(decStop - (i-1) +1);
                cnt -= preEnd;
            } else {
                cnt += sumToN(decStop - i +1);
            }
            preInc = false;
            i = decStop + 1;
        }else if((i == incStop) && (i == decStop)){ // flat case
            if((i -1)>= 0 && (ratings[i-1] < ratings[i])){
                cnt++;
            }
            cnt++;
            i++;    
            preInc = false;
        }else if((incStop > i) && (i == decStop)){ // increasing case
            cnt += sumToN(incStop - i + 1);
            preEnd = incStop - i + 1;
            if((i-1 >= 0) && (ratings[i-1] < ratings[i]) ){
                cnt += incStop - i + 1;
                preEnd += 1;
            }
            i = incStop + 1;
            preInc = true;
        }

        // console.log('cnt = ', cnt);
    }
    

    return cnt;
};

/**
 * sum of 1 to n
 */
function sumToN(n) {
    return n * (n+1) / 2    
}

/**
 * Test
 */
console.log(candy([6,5,4,3,3,2,1]));
/*
console.log(candy([58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89])); // => 208

console.log(candy([58,21,72,77,48,9,38,71,68,77,82])); // => 22
console.log(candy([58,21,72,77,48,9,38,71,68,77,82, 47,25,94,89,54,26,54,54,99,64])); // => 41 
console.log(candy([0,1,2,3,2,1])); // => 13
console.log(candy([29,51,87,87,72,12])); // => 12
console.log(candy([1,6,10,8,7,3,2])); // => 18
console.log(candy([10,8,6,5,6,10,8,7,3,2])); //27
console.log(candy([1,0,2])); // => 5 
console.log(candy([0,1,0])); // => 4 
console.log(candy([5,4,3,2,3,4,5])); // => 19
console.log(candy([5,4,3,2,2,3,4,5])); // => 20
console.log(candy([2,3,4,5,5,5,4,3,2])); // => 21 
console.log(candy([5,5,5,4,3,2])); // => 12 
console.log(candy([5,5,5,6,7,8])); // => 12 
*/
