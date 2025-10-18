package main

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	ans := &ListNode{}
	curr := ans
	carry := 0
	for l1 != nil || l2 != nil {
		x := 0
		if l1 != nil {
			x = l1.Val
		}
		y := 0
		if l2 != nil {
			y = l2.Val
		}
		sum := x + y + carry
		carry = sum / 10
		curr.Next = &ListNode{Val: sum % 10}
		curr = curr.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	if carry != 0 {
		curr.Next = &ListNode{Val: carry}
	}
	return ans.Next
}

func main() {
	testCases := []struct {
		l1 *ListNode
		l2 *ListNode
		expected *ListNode
	}{
		{l1: nil, l2: nil, expected: nil},
		{// 243 + 564 = 807
			l1: &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3}}}, 
			l2: &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4}}},
			expected: &ListNode{Val: 7, Next: &ListNode{Val: 0, Next: &ListNode{Val: 8}}}
		},
		{// 0 + 0 = 0
			l1: &ListNode{Val: 0},
			l2: &ListNode{Val: 0},
			expected: &ListNode{Val: 0},
		},
		{// 9999999 + 9999 = 10009988
			l1: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9}}}}}},
			l2: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9}}}},
			expected: &ListNode{Val: 8, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 0, Next: &ListNode{Val: 0, Next: &ListNode{Val: 0, Next: &ListNode{Val: 1}}}}}}}}
		},
	}
	
	for _, testCase := range testCases {
		result := addTwoNumbers(testCase.l1, testCase.l2)
		for result != nil {
			fmt.Print(result.Val, " ")
			result = result.Next
		}
		fmt.Println()
		for testCase.expected != nil {
			fmt.Print(testCase.expected.Val, " ")
			testCase.expected = testCase.expected.Next
		}
	}
}
