package main

func backtrack(nums []int, paths []int, ans *[][]int) {
	if len(nums) == 0 {
		perm := append([]int{}, paths...)
		*ans = append(*ans, perm)
		return
	}

	for i, num := range nums {
		newPaths := append(paths, num)
		subNums := append([]int{}, nums[:i]...)
		subNums = append(subNums, nums[i+1:]...)
		backtrack(subNums, newPaths, ans)
	}
}

func permute(nums []int) [][]int {
	ans := [][]int{}
	backtrack(nums, []int{}, &ans)
	return ans
}
