package main

func productExceptSelf(nums []int) []int {
	ans := make([]int, len(nums))

	prefix := 1
	for i, num := range nums {
		ans[i] = prefix
		prefix *= num
	}

	suffix := 1
	for i := len(nums) - 1; i >= 0; i-- {
		ans[i] *= suffix
		suffix *= nums[i]
	}

	return ans
}
