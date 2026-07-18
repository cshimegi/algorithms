package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	ans := [][]int{}

	if root == nil {
		return ans
	}

	deque := []*TreeNode{root}

	for len(deque) > 0 {
		levelSize := len(deque)
		level := []int{}

		for i := range levelSize {
			node := deque[i]
			level = append(level, node.Val)

			if node.Left != nil {
				deque = append(deque, node.Left)
			}
			if node.Right != nil {
				deque = append(deque, node.Right)
			}
		}

		ans = append(ans, level)
		deque = deque[levelSize:]
	}

	return ans
}
