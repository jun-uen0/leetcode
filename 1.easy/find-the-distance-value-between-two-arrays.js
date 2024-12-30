// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

// worst code

const fn = (arr1,arr2,d) => {
  return arr1.map(el1 => {
    return arr2.map(el2 => {
      return Math.abs(el1 - el2) > d
    }).every(Boolean)
  }).filter(Boolean).length
}
console.log(fn(arr1,arr2,d))