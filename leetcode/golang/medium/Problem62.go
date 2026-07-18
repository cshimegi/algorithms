package main

func uniquePaths(m int, n int) int {
	dp := make([]int, n)
	for i := range n {
		dp[i] = 1
	}

	for range m - 1 {
		for i := 1; i < n; i++ {
			dp[i] += dp[i-1]
		}
	}

	return dp[n-1]
}
