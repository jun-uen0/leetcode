/**
 * Input: nums = [1,3,5,6], target = 7
 * Output: 4
 */

// find the position to insert
// binary search
// time: O(logn)
// space: O(1)

const searchInsert = function(nums, target) {
  let left = 0;
  let right = nums.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] > target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return left;
}

console.log(searchInsert([1,3,5,6], 3));