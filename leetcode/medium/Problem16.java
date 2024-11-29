package leetcode.medium;


import java.util.Arrays;

/**
 * Leetcode 16
 * <p>
 * Link: <a href="https://leetcode.com/problems/3sum-closest/description/">Problem</a>
 * <p>
 * Hint:
 * */
public class Problem16 {
    public static int threeSumClosest(int[] nums, int target) {
        // Sort the array in ascending order
        Arrays.sort(nums);

        int result = Integer.MAX_VALUE;
        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > target) {
                    if (Math.abs(sum - target) < Math.abs(result - target)) {
                        result = sum;
                    }
                    right--;
                } else if (sum < target) {
                    if (Math.abs(sum - target) < Math.abs(result - target)) {
                        result = sum;
                    }
                    left++;
                } else {
                    result = sum;
                    break;
                }
            }

            if (result == target) {
                break;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(threeSumClosest(new int[]{-1,2,1,-4}, 1));
        System.out.println(threeSumClosest(new int[]{0,0,0}, 1));
        System.out.println(threeSumClosest(new int[]{-3,2,-5,0,1,1,1,-2,-3}, 8));
    }
}
