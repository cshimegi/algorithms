package leetcode.java.medium;


/**
 * Leetcode 1760
 * <p>
 * Link: <a href="https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/">Problem</a>
 * <p>
 * Hint: Find upper bound and do Binary search
 * */

public class Problem1760 {
    private static boolean isValid(int mid, int[] nums, int maxOperations) {
        int count = 0;
        for (int num : nums) {
            if (num > mid) {
                // -1 because splitting 1 bag including X balls into Y bags with maximal Z balls
                // requires only Y - 1 operations
                count += (num - 1) / mid; // Integer math for efficiency
            }
        }
        return count <= maxOperations;
    }

    public static int minimumSize(int[] nums, int maxOperations) {
        // Find the upper bound of nums
        int right = 0;
        for (int num : nums) {
            right = Math.max(right, num);
        }

        // Utilize binary search to check if the mid is possible for minimizing the penalty
        // along with the given maxOperations
        int left = 1; // nums includes all elements larger than 0
        int penalty = right;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (isValid(mid, nums, maxOperations)) {
                penalty = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return penalty;
    }

    public static void main(String[] args) {
        System.out.println(minimumSize(new int[]{9}, 2));
        System.out.println(minimumSize(new int[]{2, 4, 8, 2}, 4));
        System.out.println(minimumSize(new int[]{1}, 1));
    }
}
