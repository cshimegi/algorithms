package leetcode.java.medium;


/**
 * Leetcode 24
 * <p>
 * Link: <a href="https://leetcode.com/problems/swap-nodes-in-pairs/description/">Problem</a>
 * <p>
 * Hint:
 * */

public class Problem24 {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;
            // put second node on first node position
            prev.next = second;
            // make the next node of the original first node point to the next node of the original second node
            // ex: 1 (first)->2 (first.next) => 1 (first)->3 (second.next)
            first.next = second.next;
            // make the next node of the original second node point to the original first node
            // ex: 1->2 (second) => 2 (second)->1 (first); overall, 2->1->3->4->....
            second.next = first;
            // move to the next pair
            prev = first;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode case1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        ListNode result1 = swapPairs(case1);
        for (ListNode node = result1; node != null; node = node.next) {
            System.out.print(node.val + " ");
        }

        System.out.println();

        ListNode case2 = new ListNode(1, new ListNode(2, new ListNode(3)));
        ListNode result2 = swapPairs(case2);
        for (ListNode node = result2; node != null; node = node.next) {
            System.out.print(node.val + " ");
        }
    }
}
