package main

func reverse(x int) int {
	isNegative := x < 0
	if isNegative {
		x *= -1
	}

	ans := 0

	for x > 0 {
		ans = ans*10 + x%10
		x /= 10
	}

	if isNegative && -ans < -(1<<31) || !isNegative && ans > (1<<31)-1 {
		return 0
	}

	if isNegative {
		ans *= -1
	}

	return ans
}
