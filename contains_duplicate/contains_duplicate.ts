// this solution is optimal but uses garbage for boolean in the hashmap
function containsDuplicate(nums: number[]): boolean {
  const existingNumbers: { [key: number]: boolean } = {};

  for (let i = 0; i < nums.length; i++) {
    if (existingNumbers[nums[i]]) {
      return true;
    }
    existingNumbers[nums[i]] = true;
  }
  return false;
}

//this solution uses a set instead of a hashmap looks a bit nicer
function containsDuplicateSet(nums: number[]): boolean {
  const existingNumbers = new Set<number>();
  for (let i = 0; i < nums.length; i++) {
    if (existingNumbers.has(nums[i])) {
      return true;
    }
    existingNumbers.add(nums[i]);
  }
  return false;
}
