package leetcode.java.easy;

import java.util.Collections;
import java.util.PriorityQueue;

/**
 * Leetcode 2558
 * <p>
 * Link: <a href="https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/">Problem</a>
 * <p>
 * Hint: PriorityQueue will sort the elements in descending order every time when add new element
 * */
public class Problem2558 {
    public static long pickGifts(int[] gifts, int k)  {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int val : gifts) {
            pq.add(val);
        }

        for (int i = 0; i < k; i++) {
            // Pop max element
            int maxNum = pq.poll();
            // Update element
            pq.add((int) Math.sqrt(maxNum));
        }

        // Sum all elements
        long sum = 0;
        for (int val : pq) {
            sum += val;
        }
        return sum;
    }

    public static void main(String[] args) {
        long result = pickGifts(new int[]{25, 64, 9, 4, 100}, 4);
        System.out.println(result);

        long result2 = pickGifts(new int[]{1, 1, 1, 1}, 4);
        System.out.println(result2);
    }
}
