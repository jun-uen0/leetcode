// https://leetcode.com/problems/plus-one/

// ## Description
// You are given a large integer represented as an integer array digits,
// where each digits[i] is the ith digit of the integer.
// The digits are ordered from most significant to least significant in left-to-right order.
// The large integer does not contain any leading 0's.
// Increment the large integer by one and return the resulting array of digits.
// # 訳:
// 整数の配列digitsが与えられる。
// digits[i]は整数のi番目の桁を表す。
// 桁は左から右に最も重要なものから最も重要でないものの順に並んでいる。
// 整数には先頭の0は含まれない。
// 整数を1増やして、その結果の桁の配列を返せ。

// ## Examples
// # Example 1:
// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Incrementing by one gives 123 + 1 = 124.
// Thus, the result should be [1,2,4].
// # Example 2:
// Input: digits = [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.
// Incrementing by one gives 4321 + 1 = 4322.
// Thus, the result should be [4,3,2,2].
// # Example 3:
// Input: digits = [9]
// Output: [1,0]
// Explanation: The array represents the integer 9.
// Incrementing by one gives 9 + 1 = 10.
// Thus, the result should be [1,0].

// ## Constraints:
// 1 <= digits.length <= 100
// 0 <= digits[i] <= 9
// digits does not contain any leading 0's.

// ## My Note
// - Ignore all elements except last two elements
// - Ignore the second element from the last if the last element is 1-8
// - Add one to the second element from the last if the last element is 9
// ※ If digits is [9,9,9], the result should be [1,0,0,0]
// So that in case, I can't ignore all elements except last two elements

// digits = [1,2,3]

import java.util.Arrays;

public class PlusOne {
  public static void main(String args[]) {
    // new Solution().plusOne(new int[] { 1, 2, 3 });
    // new Solution().plusOne(new int[] { 9, 9, 9 });
    new Solution().plusOne(new int[] {5,6,2,0,0,4,6,2,4,9});
  }
}

class Solution {
  public int[] plusOne(int[] digits) {
    int carry = 1; // Add one to the last element
    
    // Loop from the last element
    for (int i = digits.length - 1; i >= 0; i--) {
      int sum = digits[i] + carry; // Ex. 9 + 1 = 10 | 1 + 1 = 2
      digits[i] = sum % 10; // Ex. 10 % 10 = 0 | 2 % 10 = 2
      carry = sum / 10; // Ex. 10 / 10 = 1 | 2 / 10 = 0
      if (carry == 0) {
        break; // If carry is 0, no need to loop anymore
      }
    }

    // Ex. [9,9,9] -> [1,0,0,0]
    if (carry != 0) {
      int[] newDigits = new int[digits.length + 1]; // To add one more element
      newDigits[0] = carry; // In this if statement, carry is always 1

      // Loop from the second element
      for (int i = 1; i < newDigits.length; i++) {
        newDigits[i] = digits[i - 1]; // Ex. newDigits[1] = digits[0]
      }
      digits = newDigits;
    }

    System.out.println(Arrays.toString(digits));
    return digits;
  }
}

// class Solution {
//   public int[] plusOne(int[] digits) {
//     int last = digits[digits.length-1];
//     if (last == 9) {
//       int num = 0;
//       for (int i=0;i<digits.length;i++) {
//         num = num * 10 + digits[i];
//       }
//       num++;
//       int[] arr = new int[String.valueOf(num).length()];
//       for (int i = arr.length - 1; i >=0; i--) {
//         arr[i] = num % 10;
//         num /= 10;
//       }
//       digits = arr;
//     } else {
//       digits[digits.length - 1] = digits[digits.length - 1] + 1;
//     }

//     System.out.println(Arrays.toString(digits));
//     return digits;
//   }
// }
