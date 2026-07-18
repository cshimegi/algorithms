package main

/**
 * Definition for singly-linked list.
 *
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	ans := &ListNode{Val: 0, Next: head}
	slow, fast := ans, ans

	for range n + 1 {
		fast = fast.Next
	}

	for fast != nil {
		slow = slow.Next
		fast = fast.Next
	}

	slow.Next = slow.Next.Next

	return ans.Next
}
