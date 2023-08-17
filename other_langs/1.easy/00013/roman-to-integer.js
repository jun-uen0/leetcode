// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.

// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

// const input = "MCMXCIV"
const input = "DCXXI"

const toArray = (str) => {
  return str.split('')
}

let split = toArray(input)
let arr = []
split.reduce( (acc, curr, idx) => {
  console.log("acc: ", acc)
  console.log("curr:", curr)
  console.log("idx: ", idx)
  console.log("------------------------")
  if (acc === 'I') {
    if(curr === 'V') {
      if(arr[arr.length -1] === 'I') {
        arr.pop()
      }  
      arr.push('IV')
      return curr
    } else if (curr === 'X') {
      if(arr[arr.length -1] === 'I') {
        arr.pop()
      } 
      arr.push('IX')
      return curr
    } else {
      arr.push(curr)
      return curr
    }
  } 
  if (acc === 'X') {
    if(curr === 'L') {
      if(arr[arr.length -1] === 'X') {
        arr.pop()
      } 
      arr.push('XL')
      return curr
    } else if (curr === 'C') {
      if(arr[arr.length -1] === 'X') {
        arr.pop()
      } 
      arr.push('XC')
      return curr
    } else {
      arr.push(curr)
      return curr
    }
  }
  if (acc === 'C') {
    if(curr === 'D') {
      if(arr[arr.length -1] === 'C') {
        arr.pop()
      } 
      arr.push('CD')
      return
    } else if (curr === 'M') {
      if(arr[arr.length -1] === 'C') {
        arr.pop()
      } 
      arr.push('CM')
      return
    } else {
      arr.push(curr)
      return curr
    }
  }
  else {
    arr.push(curr)
    return curr
  }
}, '')

const toVal = (str) => {
  return str.map( (item) => {
    if (item === 'I') return 1
    if (item === 'IV') return 4
    if (item === 'IX') return 9
    if (item === 'V') return 5
    if (item === 'X') return 10
    if (item === 'XL') return 40
    if (item === 'XC') return 90
    if (item === 'L') return 50
    if (item === 'C') return 100
    if (item === 'CD') return 400
    if (item === 'CM') return 900
    if (item === 'D') return 500
    if (item === 'M') return 1000
  })
}

const valArr = toVal(arr)
console.log(valArr)
const sum = valArr.reduce( (acc, curr) => {
  return acc + curr
}, 0)
console.log(sum)

