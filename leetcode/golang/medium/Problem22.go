package main

func backtrack(temp string, open int, close int, ans *[]string) {
	if open == 0 && close == 0 {
		*ans = append(*ans, temp)
		return
	}

	if open > 0 {
		backtrack(temp+"(", open-1, close, ans)
	}

	if open < close {
		backtrack(temp+")", open, close-1, ans)
	}
}

func generateParenthesis(n int) []string {
	ans := []string{}
	backtrack("", n, n, &ans)
	return ans
}
