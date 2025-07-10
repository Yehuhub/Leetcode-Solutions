function twoSum(nums: number[], target: number): number[] {
  const result: { [key: number]: number } = {};

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (complement in result) {
      return [result[complement], i];
    }

    result[nums[i]] = i;
  }
  return [0, 1];
}
