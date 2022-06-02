/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */

 var guess = function(num) {
  return num
}

// n <- guess
let guessNum = 0
let start = 1
let end = 2147483647

var guessNumber = function(n) {
  
//   if(n === 2) {
//     if (guess(n) === 0) {
//       guessNum = n
//       return guessNum
//     } else {
//       guessNum = 1
//       return guessNum
//     }
//   }
  
//   end = n
//   if (guess(end) === 0) {
//     guessNum = end
//     return guessNum
//   }
  
//   guessNum = Math.floor((end - start)/2) + start
  
//   if (guess(guessNum) === 0) {
//     return guessNum 
//   } else if (guess(guessNum)　=== -1) {
//     end = guessNum
//     console.log(end)
//     guessNumber(end)
//   } else if (guess(guessNum) === 1) {
//     start = guessNum
//     console.log(end)
//     guessNumber(end)
//   } else {
//     console.error("Error")
//   }
//   return guessNum
  var guessNumber = function(n) {
    let left = 1, right = n

    while(left < right) {
        const mid = left + Math.floor((right-left)/2)
        const current = guess(mid)
        if(current === 0) return mid
        if(current === -1) right = mid
        else left = mid+1
    }
    return left
  }
  return guessNumber(n)
};