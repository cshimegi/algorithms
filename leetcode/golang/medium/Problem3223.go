package main

import "fmt"

// Hint: consider the frequency of each character
func minimumLength(s string) int {
	if len(s) < 3 {
		return len(s)
	}

	f := make([]int, 26)
	for _, c := range s {
		f[c-'a']++
	}

	ans := 0
	for _, v := range f {
		if v%2 == 1 {
			ans += 1
		} else {
			if v > 2 {
				ans += 2
			} else {
				ans += v
			}
		}
	}
	return ans
}

// Leetcode 3223
// Link: https://leetcode.com/problems/minimum-length-of-string-after-operations/description/
func main() {
	fmt.Println(minimumLength("abaacbcbb"))     // 5
	fmt.Println(minimumLength("aa"))            // 2
	fmt.Println(minimumLength("bbbbbbbbb"))     // 1
	fmt.Println(minimumLength("bbbbbbbb"))      // 2
	fmt.Println(minimumLength("asndwakksoksq")) // 9
}
