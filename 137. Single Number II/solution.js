/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in obj) {
      if (obj[nums[i]] === 1) obj[nums[i]]++;
      else delete obj[nums[i]];
    } else obj[nums[i]] = 1;
  }
  let k = Object.keys(obj);
  return k[0];
};
