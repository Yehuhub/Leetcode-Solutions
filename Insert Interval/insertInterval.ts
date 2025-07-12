function insert(intervals: number[][], newInterval: number[]): number[][] {
  let result: number[][] = [];

  let i: number = 0;

  //first we insert every interval that our new interval is not in the range of to the result.
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }

  // now we merge, we make the new interval with the range of the interval we reached so far.
  // always picking the min from our new interval and the one we reached, and the max as well.
  // this guarantee we merge intervals correctly
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    newInterval = [
      Math.min(intervals[i][0], newInterval[0]),
      Math.max(intervals[i][1], newInterval[1]),
    ];
    i++;
  }
  result.push(newInterval);

  // lastly we insert all other intervals that the new interval is not in their range
  while (i < intervals.length) {
    result.push(intervals[i]);
    i++;
  }

  return result;
}
