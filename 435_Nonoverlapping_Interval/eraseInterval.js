/**
 * @param {number[][]} intervals
 * @return {number}
 */

/**
 * Sort intervals by end, 
 * the start then doesn't matter. 
 * common mistake is to sort by start, but it will remove uncessary intervals like: 
 * [[0,4], [1,2], [2, 3], [3,4]]
 */
var eraseOverlapIntervals = function(intervals) {
    // sort intervals by end   
    intervals.sort((intv1, intv2) => 
        intv1[1] - intv2[1]
    );
    console.log(intervals);

    // compare the current interval with previously non removed one
    let cur;
    let pre = intervals[0];
    let cnt = 0;
    for(i = 1; i < intervals.length; i++){
        cur = intervals[i];
        // overlap
        if(cur[0] < pre[1]){
            cnt++; 
            // do not update pre since this one is considered removed
        } else {
            pre = cur;
        } 
    }
    return cnt;
};


/*
 * Test
 */
console.log(eraseOverlapIntervals([[2.5, 4], [2,3], [1,3]])); // => 3
console.log(eraseOverlapIntervals([[1,2], [1,3], [1,9], [2,4], [2,6]])); // => 3
console.log(eraseOverlapIntervals([[0,4], [1,2], [2, 3], [3,4]])); // => 1
