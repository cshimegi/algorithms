package main

import "fmt"

func binarySearch(nums []int, target int, findLowest bool) int {
	l := len(nums)
	if l == 0 {
		return -1
	}

	low := 0
	high := l - 1
	ans := -1
	for low <= high {
		mid := low + (high-low)/2
		if nums[mid] == target {
			if ans == -1 {
				ans = mid
			} else {
				if findLowest {
					if mid < ans {
						ans = mid
					}
					high = mid - 1
				} else {
					if mid > ans {
						ans = mid
					}
					low = mid + 1
				}
			}
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return ans
}

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	ranges := []int{-1, -1}
	ranges[0] = binarySearch(nums, target, true)
	ranges[1] = binarySearch(nums, target, false)
	return ranges
}

// Leetcode 34
// Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
func main() {
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 8))
	fmt.Println(searchRange([]int{8, 8, 8, 8, 8, 8}, 8))
}
