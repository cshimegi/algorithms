package main

func minSubArrayLen(target int, nums []int) int {
	l := len(nums)

	check := func(possibleLen int) bool {
		sum := 0
		for _, num := range nums[:possibleLen] {
			sum += num
		}
		if sum >= target {
			return true
		}

		for i := possibleLen; i < l; i++ {
			sum += nums[i] - nums[i-possibleLen]
			if sum >= target {
				return true
			}
		}

		return false
	}

	k, r := 1, l
	for k < r {
		mid := (k + r) / 2
		if check(mid) {
			r = mid
		} else {
			k = mid + 1
		}
	}

	if check(k) {
		return k
	}

	return 0
}
