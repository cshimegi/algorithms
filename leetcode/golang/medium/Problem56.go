package main

import "sort"

func merge(intervals [][]int) [][]int {
	if len(intervals) == 1 {
		return intervals
	}

	sort.Slice(intervals, func(prevIdx, nextIdx int) bool {
		return intervals[prevIdx][0] < intervals[nextIdx][0]
	})

	ans := [][]int{}

	for _, interval := range intervals {
		lastIdx := len(ans) - 1
		if len(ans) == 0 || ans[lastIdx][1] < interval[0] {
			ans = append(ans, interval)
		} else {
			if ans[lastIdx][1] < interval[1] {
				ans[lastIdx][1] = interval[1]
			}
		}
	}

	return ans
}
