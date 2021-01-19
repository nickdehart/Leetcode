/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  nums.sort((a, b) => a - b);

  const ans = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let ii = i + 1;
    let iii = nums.length - 1;

    while (ii < iii) {
      if (nums[i] + nums[ii] + nums[iii] === 0) {
        ans.push([nums[i], nums[ii], nums[iii]]);
        ii += 1;
        iii -= 1;
        while (ii < iii && nums[ii] === nums[ii - 1]) ii += 1;
        while (ii < iii && nums[iii] === nums[iii + 1]) iii -= 1;
      } else if (nums[i] + nums[ii] + nums[iii] < 0) ii++;
      else iii--;
    }
  }
  return ans;
};
