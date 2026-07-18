package main

func minPathSum(grid [][]int) int {
	r, c := len(grid), len(grid[0])
	for i := 1; i < r; i++ {
		grid[i][0] += grid[i-1][0]
	}

	for i := 1; i < c; i++ {
		grid[0][i] += grid[0][i-1]
	}

	for i := 1; i < r; i++ {
		for j := 1; j < c; j++ {
			min := grid[i-1][j]
			if grid[i][j-1] < min {
				min = grid[i][j-1]
			}
			grid[i][j] += min
		}
	}

	return grid[r-1][c-1]
}
