package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValid(node *TreeNode, lower, upper int) bool {
	if node == nil {
		return true
	}

	if lower < node.Val && node.Val < upper {
		return isValid(node.Left, lower, node.Val) && isValid(node.Right, node.Val, upper)
	}

	return false
}

func isValidBST(root *TreeNode) bool {
	return isValid(root, -(1 << 32), 1<<32-1)
}
