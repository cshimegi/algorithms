package leetcode.java.medium;


import java.util.Arrays;

/**
 * Leetcode 31
 * <p>
 * Link: <a href="https://leetcode.com/problems/next-permutation/description/">Problem</a>
 * <p>
 * Hint:
 * */

public class Problem31 {
    public static void nextPermutation(int[] nums) {
        int n = nums.length;
        // Find the rightmost descending point
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            // Swap nums[i] with the smallest larger number on the right
            int j = n - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }

        // Reverse the remaining numbers to the right of i
        int l = i + 1;
        int r = n - 1;
        while (l < r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }

    public static void main(String[] args) {
        int[] nums1 = new int[]{1, 2, 3};
        nextPermutation(nums1);
        System.out.println(Arrays.toString(nums1)); // 1 3 2

        int[] nums2 = new int[]{3, 2, 1};
        nextPermutation(nums2);
        System.out.println(Arrays.toString(nums2)); // 1 2 3

        int[] nums3 = new int[]{1, 1, 5};
        nextPermutation(nums3);
        System.out.println(Arrays.toString(nums3)); // 1 5 1

        int[] nums4 = new int[]{1, 3, 2, 4};
        nextPermutation(nums4);
        System.out.println(Arrays.toString(nums4)); // 1 3 4 2

        int[] nums5 = new int[]{1, 5, 1};
        nextPermutation(nums5);
        System.out.println(Arrays.toString(nums5)); // 5 1 1

        int[] nums6 = new int[]{1};
        nextPermutation(nums6);
        System.out.println(Arrays.toString(nums6)); // 1

        int[] nums7 = new int[]{1, 3, 2};
        nextPermutation(nums7);
        System.out.println(Arrays.toString(nums7)); // 2 1 3
    }
}
