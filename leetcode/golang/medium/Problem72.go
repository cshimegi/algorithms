package main

func minDistance(word1 string, word2 string) int {
	r, c := len(word1), len(word2)
	dp := make([][]int, r+1)
	for i := range r + 1 {
		dp[i] = make([]int, c+1)
	}

	for i := range r + 1 {
		dp[i][0] = i
	}

	for j := range c + 1 {
		dp[0][j] = j
	}

	for i := 1; i < r+1; i++ {
		for j := 1; j < c+1; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				min := dp[i-1][j-1]
				if dp[i-1][j] < dp[i][j-1] && dp[i-1][j] < min {
					min = dp[i-1][j]
				} else if dp[i][j-1] < dp[i-1][j] && dp[i][j-1] < min {
					min = dp[i][j-1]
				}

				dp[i][j] = min + 1
			}
		}
	}

	return dp[r][c]
}
