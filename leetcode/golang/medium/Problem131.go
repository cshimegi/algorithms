package main

import "fmt"

func isPalindrome(s string) bool {
	l := len(s)
	for i := 0; i < l/2; i++ {
		if s[i] != s[l-i-1] {
			return false
		}
	}
	return true
}

func partition(s string) [][]string {
	l := len(s)
	if l == 0 {
		return [][]string{{}}
	} else if l == 1 {
		return [][]string{{s}}
	}

	results := make([][]string, 0, l)
	for i := 0; i < l; i++ {
		if isPalindrome(s[:i+1]) {
			for _, r := range partition(s[i+1:]) {
				results = append(results, append([]string{s[:i+1]}, r...))
			}
		}
	}
	return results
}

// Leetcode 131
// Link: https://leetcode.com/problems/palindrome-partitioning/description/
func main() {
	fmt.Println(partition("abba"))
}
