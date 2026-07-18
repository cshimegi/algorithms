package main

func wordBreak(s string, wordDict []string) bool {
	maxLen := 0
	maps := map[string]bool{}
	for _, word := range wordDict {
		maps[word] = true

		lenWord := len(word)
		if lenWord > maxLen {
			maxLen = lenWord
		}
	}

	ls := len(s)
	dp := make([]bool, ls+1)
	dp[0] = true
	for i := 0; i < ls+1; i++ {
		startIdx := i - maxLen
		if startIdx < 0 {
			startIdx = 0
		}

		for j := startIdx; j < i; j++ {
			if dp[j] && maps[s[j:i]] {
				dp[i] = true
				break
			}
		}
	}

	return dp[ls]
}
