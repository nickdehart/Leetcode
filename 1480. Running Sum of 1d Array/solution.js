/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
  let a = [];
  let temp = 0;
  for (let i = 0; i < nums.length; i++) {
    temp += nums[i];
    a.push(temp);
  }
  return a;
};
