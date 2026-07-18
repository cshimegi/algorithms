package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func merge(node1 *ListNode, node2 *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	for node1 != nil && node2 != nil {
		if node1.Val < node2.Val {
			curr.Next = node1
			node1 = node1.Next
		} else {
			curr.Next = node2
			node2 = node2.Next
		}
		curr = curr.Next
	}

	if node1 != nil {
		curr.Next = node1
	}

	if node2 != nil {
		curr.Next = node2
	}

	return dummy.Next
}

func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	slow := head
	fast := head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	mid := slow.Next
	slow.Next = nil

	left := sortList(head)
	right := sortList(mid)

	return merge(left, right)
}
