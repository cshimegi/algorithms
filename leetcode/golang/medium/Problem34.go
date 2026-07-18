package main

import "fmt"

func binarySearch(nums []int, target int, findLowest bool) int {
	ans, l, r := -1, 0, len(nums)-1

	for l <= r {
		mid := (l + r) / 2
		if nums[mid] == target {
			ans = mid

			if findLowest {
				r = mid - 1
			} else {
				l = mid + 1
			}
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return ans
}

func searchRange(nums []int, target int) []int {
	a := binarySearch(nums, target, true)
	b := binarySearch(nums, target, false)

	return []int{a, b}
}

// Leetcode 34
// Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
func main() {
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 8))
	fmt.Println(searchRange([]int{8, 8, 8, 8, 8, 8}, 8))
}
