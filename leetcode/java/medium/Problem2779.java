package leetcode.java.medium;


import java.util.Arrays;

/**
 * Leetcode 2779
 * <p>
 * Link: <a href="https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/">Problem</a>
 * <p>
 * Hint: Use sliding window to find maximum subarray A[i … j] such that A[j] - A[i] ≤ 2 * k after sorting the array
 * */

public class Problem2779 {
    public static int maximumBeauty(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0;
        int r = 0;
        while (l <= r && r < nums.length) {
            if (nums[r] - nums[l] > 2 * k) {
                l++;
            }
            r++;
        }
        return r - l;
    }

    private static int binarySearch(int[] nums, int limit) {
        int low = 0, high = nums.length;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] > limit) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low; // This is the first index where nums[index] > limit
    }

    public static int optimizedMaximumBeauty(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int result = 0;

        for (int i = 0; i < n; i++) {
            // Use binary search to find the first element > nums[i] + 2 * k
            int limit = nums[i] + 2 * k;
            int j = binarySearch(nums, limit);
            result = Math.max(result, j - i);
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(maximumBeauty(new int[]{4, 6, 1, 2}, 2)); // 3
        System.out.println(maximumBeauty(new int[]{1, 1, 1, 1}, 10)); // 4
        System.out.println(maximumBeauty(new int[]{1, 4, 7, 10, 13, 16, 19, 22, 25}, 1)); // 1
        System.out.println(maximumBeauty(new int[]{0, 2, 0, 3}, 0)); // 2

        System.out.println("======================");

        System.out.println(optimizedMaximumBeauty(new int[]{4, 6, 1, 2}, 2)); // 3
        System.out.println(optimizedMaximumBeauty(new int[]{1, 1, 1, 1}, 10)); // 4
        System.out.println(optimizedMaximumBeauty(new int[]{1, 4, 7, 10, 13, 16, 19, 22, 25}, 1)); // 1
        System.out.println(optimizedMaximumBeauty(new int[]{0, 2, 0, 3}, 0)); // 2
    }
}
