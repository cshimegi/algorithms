package main

import (
	"fmt"
)

// Requirement: O(log n) performance
// Hint:
func search(nums []int, target int) int {
	low, high := 0, len(nums)-1
	for low <= high {
		mid := low + (high-low)/2
		if nums[mid] == target {
			return mid
		}

		if nums[low] <= nums[mid] {
			if nums[low] <= target && target < nums[mid] {
				high = mid - 1
			} else {
				low = mid + 1
			}
		} else {
			// Large numbers are on left side
			if nums[mid] < target && target <= nums[high] {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}
	}

	return -1
}

// Leetcode 33
// Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
func main() {
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 0))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 3))
	fmt.Println(search([]int{1}, 0))
}
