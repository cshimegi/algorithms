package leetcode.java.medium;

import java.util.HashMap;
import java.util.stream.IntStream;


/**
 * Leetcode 2461
 * <p>
 * Link: <a href="https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/">Problem</a>
 * <p>
 * Hint: Use sliding window to record frequencies and calculate sum simultaneously -> optimizedMaximumSubarraySum
 * */
public class Problem2461 {
    /**
     * Worse performance: O(n^2)
     * */
    public static long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        // Find the maximum subarray sum
        long result = 0;
        for (int r = k-1; r < n; r++) {
            // Get the left pointer
            int l = r - k + 1;
            // Flag to know if all elements are unique
            boolean ok = true;
            // Record the frequencies of the numbers in the subarray
            HashMap<Integer, Integer> freq = new HashMap<>();
            for (int i = l; i <= r; i++) {
                freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
                if (freq.get(nums[i]) > 1) {
                    // Element already exists in the window
                    ok = false;
                    break;
                }
            }

            // When all elements are unique
            if (ok) {
                // Sum the subarray from l to r without overflow
                long sum = IntStream.range(l, r + 1).mapToLong(i -> nums[i]).sum();
                result = Math.max(result, sum);
            }
        }
        return result;
    }

    /**
     * Better performance with sliding window: O(n)
     * */
    public static long optimizedMaximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long answer = 0;
        long currentSum = 0;
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int r = 0; r < n; r++) {
            // Record the frequencies of the numbers in the subarray
            freq.put(nums[r], freq.getOrDefault(nums[r], 0) + 1);
            // Update the current sum
            currentSum += nums[r];
            // If the window size exceeds k, shrink it from the left
            if (r >= k) {
                int left = nums[r-k];
                freq.put(left, freq.get(left) - 1);
                if (freq.get(left) == 0) {
                    // Remove the element from the map because we need to know if freq
                    // records all unique k elements
                    freq.remove(left);
                }
                currentSum -= left;
            }
            // Update the answer with maximum sum
            if (freq.size() == k) {
                answer = Math.max(answer, currentSum);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(maximumSubarraySum(new int[]{9,9,9}, 3));
        System.out.println(maximumSubarraySum(new int[]{1,5,4,2,9,9,9}, 3));
        System.out.println(maximumSubarraySum(new int[]{1,2,3,4,5,6,7,8,9,10}, 10));

        // generate an array with elements from 1 to 100000
        int[] arr = IntStream.rangeClosed(1, 100000).toArray();
        System.out.println(optimizedMaximumSubarraySum(arr, 100000));
        System.out.println(optimizedMaximumSubarraySum(new int[]{1,2,3,4,5,6,7,8,9,10,10}, 10));
    }
}
