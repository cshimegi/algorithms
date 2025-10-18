package main

import "strings"

func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}

	split_s := strings.Split(s, "")
	new_s := "#" + strings.Join(split_s, "#") + "#"
	news_s_l := len(new_s)
	max_len := 0
	ans := ""

	for i := range news_s_l {
		r := 0
		for i+r < news_s_l && i-r >= 0 && new_s[i+r] == new_s[i-r] {
			r += 1
		}

		if 2*(r-1)+1 > max_len {
			max_len = 2*(r-1) + 1
			ans = new_s[i-r+1 : i+r]
		}
	}

	return strings.ReplaceAll(ans, "#", "")
}
