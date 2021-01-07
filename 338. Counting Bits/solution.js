/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
  let a = [];
  for (let i = 0; i <= num; i++) {
    let k = i;
    let count = 0;
    while (k) {
      k &= k - 1;
      count += 1;
    }
    a.push(count);
  }
  return a;
};
