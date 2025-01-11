package main

import "fmt"

// Hint: If the number of characters that have odd counts is > k then the minimum number
// of palindrome strings we can construct is > k and answer is false.
func canConstruct(s string, k int) bool {
	if k > len(s) {
		return false
	}

	records := make([]int, 26)
	for _, c := range s {
		records[c-'a']++
	}

	oddsCount := 0
	for _, v := range records {
		if v%2 == 1 {
			oddsCount++
		}
	}

	return oddsCount <= k
}

// Leetcode 131
// Link: https://leetcode.com/problems/palindrome-partitioning/description/
func main() {
	fmt.Println(canConstruct("annabelle", 2))
	fmt.Println(canConstruct("leetcode", 3))
	fmt.Println(canConstruct("true", 4))
}
