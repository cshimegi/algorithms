package leetcode.java.medium;


import java.util.Arrays;

/**
 * Leetcode 3152
 * <p>
 * Link: <a href="https://leetcode.com/problems/special-array-ii/description/">Problem</a>
 * <p>
 * Hint: Precompute the accumulated parity and check the number of accumulated parity
 * */

public class Problem3152 {
    public static boolean[] isArraySpecial(int[] nums, int[][] queries)  {
        int n = nums.length;
        // Record the accumulation if parity is the same
        int[] accumulation = new int[n];
        accumulation[0] = 0;
        for (int i = 1; i < n; i++) {
            accumulation[i] = accumulation[i-1];
            if (nums[i-1] % 2 != nums[i] % 2) {
                accumulation[i]++;
            }
        }

        // Check if the number of accumulated parity is the same as the number of elements in
        // the specified range (l, r). If so, the array is special array
        int m = queries.length;
        boolean[] res = new boolean[m];
        for (int i = 0; i < m; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            res[i] = (accumulation[r] - accumulation[l]) == (r-l);
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums1 = new int[]{3, 4, 1, 2, 6};
        int[][] queries1 = new int[][]{{0, 4}, {1, 3}, {0, 2}};
        boolean[] result1 = isArraySpecial(nums1, queries1);
        System.out.println(Arrays.toString(result1));

        int[] nums2 = new int[]{4,3,1,6};
        int[][] queries2 = new int[][]{{0, 2}, {2, 3}};
        boolean[] result2 = isArraySpecial(nums2, queries2);
        System.out.println(Arrays.toString(result2));
    }
}
