package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Hint:
func countAndSay(n int) string {
	ans := "1"

	for i := 2; i <= n; i++ {
		l := len(ans)
		k := 0
		var temp strings.Builder
		for j := 1; j < l; j++ {
			if ans[j-1] == ans[j] {
				continue
			}
			temp.WriteString(strconv.Itoa(j - 1 - k + 1))
			temp.WriteString(string(ans[k]))
			k = j
		}
		// Append the last sequence of characters
		temp.WriteString(strconv.Itoa(l - k))
		temp.WriteString(string(ans[k]))
		ans = temp.String()
	}

	return ans
}

// Leetcode 38
// Link: https://leetcode.com/problems/count-and-say/description/
func main() {
	fmt.Println(countAndSay(1))  // "1"
	fmt.Println(countAndSay(4))  // "1211"
	fmt.Println(countAndSay(7))  // "13112221"
	fmt.Println(countAndSay(10)) // "13211311123113112211"
}
