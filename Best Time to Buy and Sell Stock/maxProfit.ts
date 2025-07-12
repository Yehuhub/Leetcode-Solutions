// naive solution o(n^2), find all pairs
// return the max

// in this solution, we always keep the minimum value seen, then for future values to be max profit
// they have to be calculated with the min number seen so far.
function maxProfit(prices: number[]): number {
  let minSeen: number = prices[0];
  let maxProf: number = 0;

  for (let i = 1; i < prices.length; i++) {
    const currentProfit: number = prices[i] - minSeen;
    maxProf = Math.max(currentProfit, maxProf);
    minSeen = Math.min(prices[i], minSeen);
  }
  return maxProf;
}

// this solution uses two pointers to find the maxprofit
function maxProfitTwoPointer(prices: number[]): number {
  let buy: number = 0;
  let sell: number = 1;
  let max: number = 0;

  while (sell < prices.length) {
    if (prices[buy] < prices[sell]) {
      const profit: number = prices[sell] - prices[buy];
      max = Math.max(profit, max);
    } else {
      buy = sell;
    }
    sell++;
  }
  return max; // max is zero unless the profit is positive
}
