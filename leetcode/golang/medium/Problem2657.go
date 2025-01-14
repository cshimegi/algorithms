package main

import (
	"fmt"
)

// Hint:
func findThePrefixCommonArray(A []int, B []int) []int {
	l := len(A)
	freq := make(map[int]int, l)
	ans := [50]int{}
	common := 0
	for i := 0; i < l; i++ {
		freq[A[i]]++
		freq[B[i]]++
		if A[i] == B[i] {
			common++
		} else {
			if freq[A[i]] == 2 {
				common++
			}
			if freq[B[i]] == 2 {
				common++
			}
		}
		ans[i] = common
	}
	return ans[:l]
}

// Leetcode 2657
// Link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
func main() {
	fmt.Println(findThePrefixCommonArray([]int{1, 3, 2, 4}, []int{3, 1, 2, 4}))
	fmt.Println(findThePrefixCommonArray([]int{2, 3, 1}, []int{3, 1, 2}))
}
