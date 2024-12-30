// https://leetcode.com/problems/binary-search/

/**
 * Given an array of integers nums which is sorted in ascending order,
 * and an integer target, write a function to search target in nums.
 * If target exists, then return its index. Otherwise, return -1.
 * You must write an algorithm with O(log n) runtime complexity.
 */

/** 
 * Example 1:
 * Input: nums = [-1,0,3,5,9,12], target = 9
 * Output: 4
 * Explanation: 9 exists in nums and its index is 4
 */

/**
 * Example 2:
 * Input: nums = [-1,0,3,5,9,12], target = 2
 * Output: -1
 * Explanation: 2 does not exist in nums so return -1
 */

let idx = 0

function binarySearch (arr, target) {

  if (arr.length === 0) {
    if(arr[0] === target) {
      return idx
    } else {
      return -1
    }
  }

  const mid = Math.floor(arr.length / 2)
  const pivot = arr[mid]

  if (pivot === target) {
    idx += mid
    return idx
  }

  if (pivot > target) {
    const left = arr.slice(0, mid)
    return binarySearch(left, target)
  }

  if (pivot < target) {
    const right = arr.slice(mid + 1)
    idx += mid + 1
    return binarySearch(right, target)
  }
  return
}

console.log(binarySearch([-1,0,3,5,9,12], 9))