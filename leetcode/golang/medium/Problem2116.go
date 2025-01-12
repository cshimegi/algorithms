package main

import "fmt"

// Hint: Don't overthink and just check from both sides
func canBeValid(s string, locked string) bool {
	l := len(s)
	if l%2 == 1 {
		return false
	}
	// from left to right
	balance := 0
	for i := 0; i < l; i++ {
		if locked[i] == '0' || s[i] == '(' {
			balance++
		} else if s[i] == ')' {
			balance--
		}
		if balance < 0 {
			return false
		}
	}

	// from right to left
	balance = 0
	for i := l - 1; i >= 0; i-- {
		if locked[i] == '0' || s[i] == ')' {
			balance++
		} else if s[i] == '(' {
			balance--
		}
		if balance < 0 {
			return false
		}
	}

	return true
}

// Leetcode 2116
// Link: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/
func main() {
	fmt.Println(canBeValid("))()))", "010100")) // true
	fmt.Println(canBeValid("(())", "0110"))     // true
	fmt.Println(canBeValid("(())", "1111"))     // true
	fmt.Println(canBeValid("()()", "0000"))     // true
	fmt.Println(canBeValid(")", "0"))           // false
	fmt.Println(canBeValid("))))))", "000000")) // true
	fmt.Println(canBeValid("))))))", "111111")) // false
	fmt.Println(canBeValid("((((((", "000000")) // true
	fmt.Println(canBeValid("((((((", "111111")) // false
}
