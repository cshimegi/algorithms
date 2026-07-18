package main

func maxArea(height []int) int {
	ans := 0
	l, r := 0, len(height)-1
	for l < r {
		if height[l] < height[r] {
			if height[l]*(r-l) > ans {
				ans = height[l] * (r - l)
			}
			l += 1
		} else {
			if height[r]*(r-l) > ans {
				ans = height[r] * (r - l)
			}
			r -= 1
		}
	}

	return ans
}
