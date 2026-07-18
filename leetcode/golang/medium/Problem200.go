package main

func numIslands(grid [][]byte) int {
	r, c := len(grid), len(grid[0])

	directions := [][]int{[]int{1, 0}, []int{0, 1}, []int{0, -1}, []int{-1, 0}}
	var dfs func(dr, dc int)
	dfs = func(dr, dc int) {
		if 0 <= dr && dr < r && 0 <= dc && dc < c && grid[dr][dc] == '1' {
			grid[dr][dc] = '#'
			for _, d := range directions {
				dfs(dr+d[0], dc+d[1])
			}
		} else {
			return
		}
	}

	ans := 0
	for i := range r {
		for j := range c {
			if grid[i][j] == '1' {
				dfs(i, j)
				ans += 1
			}
		}
	}

	return ans
}
