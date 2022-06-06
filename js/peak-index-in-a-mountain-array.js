// https://leetcode.com/problems/peak-index-in-a-mountain-array/

/**
 * Let's call an array arr a mountain if the following properties hold:
 * arr.length >= 3
 * There exists some i with 0 < i < arr.length - 1 such that:
 * arr[0] < arr[1] < ... arr[i-1] < arr[i]
 * arr[i] > arr[i+1] > ... > arr[arr.length - 1]
 * Given an integer array arr that is "guaranteed" to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
 */

// quicksort
// 1. partitioning
// 2. recursion
// 3. base case

const partition = (arr, left, right) => {
  let pivot = arr[Math.floor((left + right) / 2)]
  while (left <= right) {
    while (arr[left] < pivot) {
      left++
    }
    while (arr[right] > pivot) {
      right--
    }
    if (left <= right) {
      [arr[left], arr[right]] = [arr[right], arr[left]]
      left++
      right--
    }
  }
  return left
}

const quickSort = (arr, left, right) => {
  if (left < right) {
    let pivot = partition(arr, left, right)
    quickSort(arr, left, pivot - 1)
    quickSort(arr, pivot + 1, right)
  }
}

const sortedArray = (arr) => {
  quickSort(arr, 0, arr.length - 1)
  return arr
}

console.log(sortedArray([6,2,3,1,5,4])) // [1,2,3,4,5,6]
