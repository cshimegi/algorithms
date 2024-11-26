package leetcode.medium;

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

/**
 * Leetcode 18
 * <p>
 * Link: <a href="https://leetcode.com/problems/4sum/description/">Problem</a>
 * <p>
 * Hint: Sort array first and change the problem to 2sum to reduce the problem to O(n^2)
 * */
public class Problem18 {
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        int n = nums.length;
        for (int i=0; i<n-2; i++) {
            // Avoid duplicates
            if (i > 0 && nums[i] == nums[i-1]) continue;

            for (int j=i+1; j<n-1; j++) {
                // Avoid duplicates
                if (j > i+1 && nums[j] == nums[j-1]) continue;

                int left = j+1;
                int right = n-1;
                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum > target) {
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        // Move pointers to avoid duplicates
                        while (left < right && nums[left] == nums[left+1]) left++;
                        while (left < right && nums[right] == nums[right-1]) right--;
                        left++;
                        right--;
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0));
    }
}
