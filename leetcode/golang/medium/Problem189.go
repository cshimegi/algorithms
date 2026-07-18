package main

// Time: O(n) / Space: O(1); Cycle math
func rotate(nums []int, k int) {
	n := len(nums)
	k %= n

	count := 0
	for start := 0; count < n; start++ {
		curr := start
		prev := nums[start]

		for {
			next := (curr + k) % n
			nums[next], prev = prev, nums[next]

			curr = next
			count++

			if curr == start {
				break
			}
		}
	}
}
