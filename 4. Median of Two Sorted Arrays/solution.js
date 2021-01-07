/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  let merged = [];
  let k = 0;
  for (let i = 0; i < nums1.length; i++) {
    while (nums2[k] < nums1[i]) {
      merged.push(nums2[k]);
      k++;
    }
    merged.push(nums1[i]);
  }
  while (k < nums2.length) {
    merged.push(nums2[k]);
    k++;
  }
  if (merged.length % 2 === 1) return merged[Math.floor(merged.length / 2)];
  return (merged[merged.length / 2 - 1] + merged[merged.length / 2]) / 2;
};
