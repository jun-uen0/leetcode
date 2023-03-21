// https://leetcode.com/problems/longest-common-prefix/

// Input: strs = ["flower","flow","flight"]
// first: "fl"

// Input: strs = ["dog","racecar","car"]
// first: ""

// Input: Vec<String>
// first: String

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters.

// let strs = ["flower","flow","flight"]

impl Solution {
  pub fn longest_common_prefix(strs: Vec<String>) -> String {
    // println!("{:?}", strs); // ["flower","flow","flight"] 

    // if using "{}" it's not working because it's not a string. It's a vector. If you want to print it, you need to use "{:?}"
    // "{:?}" means to print the vector in a pretty way (line by line)
    // "{:#?}" means to print the vector in a pretty way with virtical alignment

    let mut word = ""; // initialize the prefix to be empty string.
    for i in 0..strs.len() { 
      // println!("{}", &strs[i]);  // 'flower' 'flow' 'flight' each line is a string

      if i == 0 {
        word = &strs[i]; // if it's the first string, assign it to the word. For example, if it's 'flower', then word = 'flower'
      } else {
        let mut j = 0;
        while j < word.len() && j < strs[i].len() {
          // nth() is a method of String. It returns a char.
          // println!("{}", word.nth(j)); // 'f' 'l' 'o' 'w' 'e' 'r'
          println!("{}", word.chars().nth(j).unwrap()); // 'f' for the first string, 'l' for the second string, 'o' for the third string
          // println!("{}", strs[i].nth(j)); // 'f' 'l' 'o' 'w' // i is not 0, so it's not the first string.
          if word.chars().nth(j).unwrap() == strs[i].chars().nth(j).unwrap() {
            j += 1;
          } else {
            break; // if the first string and the second string don't have the same char, then break the loop. Go back to if i == 0
          }
        }
        word = &word[0..j];
        // if j is 3, then it will get the first 3 characters of word.
        // In Rust, & means to get the reference of the string.
        // [0..j] means to get the first j characters of word.
        // So &word[0..j] means to get the first j characters of word as a string.
      }
    }

    return word.to_string(); // return the prefix as a string while it is empty
  }
}