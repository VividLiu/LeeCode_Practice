const { logger } = require('../Utils/logger');

logger.setDebugFlag(false);

/**
 * Two pass
 */
var candy = function(ratings) {
    if(!ratings.length){
        return 0;
    }else if(ratings.length === 1){
       return 1; 
    }

    const candies = new Array(ratings.length);

    candies[0] = 1;

    // first pass: left to right
    for(let i = 1; i < candies.length; i++) {
        candies[i] = (ratings[i] > ratings[i-1] ? candies[i-1] + 1 : 1);
    }

    // second pass: right to left
    for(let i = candies.length - 2; i >= 0; i--) {
        candies[i] = (ratings[i] > ratings[i+1] ? Math.max(candies[i], candies[i+1] + 1) : candies[i]);     
    }

    logger.debug(candies);
    return candies.reduce((pre, cur) => pre + cur, 0);
};


/**
 * Test
 */
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
