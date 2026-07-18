package main

import "strconv"

func evalRPN(tokens []string) int {
	stack := []int{}

	for _, t := range tokens {
		if t == "+" || t == "-" || t == "*" || t == "/" {
			l := len(stack)
			secondNum := stack[l-1]
			firstNum := stack[l-2]
			stack = stack[:l-2]
			if t == "+" {
				stack = append(stack, firstNum+secondNum)
			} else if t == "-" {
				stack = append(stack, firstNum-secondNum)
			} else if t == "*" {
				stack = append(stack, firstNum*secondNum)
			} else {
				stack = append(stack, firstNum/secondNum)
			}
		} else {
			num, _ := strconv.Atoi(t)
			stack = append(stack, num)
		}
	}

	return stack[0]
}
