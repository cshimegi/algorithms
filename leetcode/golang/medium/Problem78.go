package main

func subsets(nums []int) [][]int {
	l, subset, ans := len(nums), []int{}, [][]int{}

	var dfs func(i int)
	dfs = func(i int) {
		if i >= l {
			curr := append([]int{}, subset...)
			ans = append(ans, curr)
			return
		}

		subset = append(subset, nums[i])
		dfs(i + 1)
		subset = subset[:len(subset)-1]
		dfs(i + 1)

	}

	dfs(0)

	return ans
}
