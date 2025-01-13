package main

import "fmt"

func backtrack(candidates []int, start int, target int, current []int, results [][]int) [][]int {
	if target == 0 {
		return append(results, append([]int{}, current...))
	}

	for i := start; i < len(candidates); i++ {
		diff := target - candidates[i]
		if diff >= 0 {
			results = backtrack(candidates, i, diff, append(current, candidates[i]), results)
		}
	}
	return results
}

// Hint: utilize start argument to avoid duplicates
func combinationSum(candidates []int, target int) [][]int {
	return backtrack(candidates, 0, target, []int{}, [][]int{})
}

// Leetcode 39
// Link: https://leetcode.com/problems/combination-sum/description/
func main() {
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
}
