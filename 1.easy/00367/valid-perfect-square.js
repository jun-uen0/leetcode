/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
  let i = 1
  while(i * i <= num + ((i - 1) * (i - 1))) {
    if(i * i === num) {
      return true
    } else if (i * i > num) {
      return false
    } else {
      i++
    }
  }
}
console.log(isPerfectSquare(5))