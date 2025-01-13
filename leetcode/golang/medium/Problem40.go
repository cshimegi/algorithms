package main

import (
	"fmt"
	"sort"
)

func backtrack2(candidates []int, target int, start int, current []int, results [][]int) [][]int {
	if target == 0 {
		return append(results, append([]int{}, current...))
	}

	for i := start; i < len(candidates); i++ {
		// avoid duplicates
		if i > start && candidates[i] == candidates[i-1] {
			continue
		}
		diff := target - candidates[i]
		if diff >= 0 {
			results = backtrack2(candidates, diff, i+1, append(current, candidates[i]), results)
		}
	}
	return results
}

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	return backtrack2(candidates, target, 0, []int{}, [][]int{})
}

// Leetcode 40
// Link: https://leetcode.com/problems/combination-sum-ii/description/
func main() {
	fmt.Println(combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8))
}
