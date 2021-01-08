/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
  let nums2 = [];
  for (let i = 0; i < nums.length; i++)
    if (nums2.includes(nums[i])) return nums[i];
    else nums2.push(nums[i]);
};
