package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	records := make(map[rune]int)
	i := 0
	ans := 0
	for j, c := range s {
		if _, ok := records[c]; ok && records[c] >= i {
			i = records[c] + 1
		}
		records[c] = j
		ans = max(ans, j-i+1)
	}
	return ans
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("bbbbb"))
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
	fmt.Println(lengthOfLongestSubstring("tmmzuxt"))
	fmt.Println(lengthOfLongestSubstring(" "))
	fmt.Println(lengthOfLongestSubstring("ckilbkd"))
	fmt.Println(lengthOfLongestSubstring("$# $"))
}
