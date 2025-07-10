// My initial solution, a bit ugly
function majorityElement(nums: number[]): number {
  let majNum = nums[0];
  let count = 1;
  for (let i = 1; i < nums.length; i++) {
    if (majNum == nums[i]) {
      count++;
    } else {
      if (count == 0) {
        majNum = nums[i];
      } else {
        count--;
      }
    }
  }
  return majNum;
}

// cleaner implementation
function majorityElementCleaner(nums: number[]): number {
  let majNum = nums[0];
  let count = 0;
  for (const num of nums) {
    if (count === 0) {
      majNum = num;
    }
    count += majNum === num ? 1 : -1;
  }
  return majNum;
}
