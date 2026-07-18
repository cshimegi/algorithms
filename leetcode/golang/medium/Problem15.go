package main

import "sort"

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	l := len(nums)
	ans := [][]int{}

	for i, num := range nums {
		if num > 0 {
			break
		}

		if i > 0 && num == nums[i-1] {
			continue
		}

		j, k := i+1, l-1
		for j < k {
			sum := num + nums[j] + nums[k]
			if sum > 0 {
				k -= 1
			} else if sum < 0 {
				j += 1
			} else {
				ans = append(ans, []int{num, nums[j], nums[k]})
				j += 1

				for j < k && nums[j] == nums[j-1] {
					j += 1
				}
			}
		}
	}

	return ans
}
