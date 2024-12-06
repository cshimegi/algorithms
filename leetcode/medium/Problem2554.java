package leetcode.medium;


import java.util.Arrays;

/**
 * Leetcode 2554
 * <p>
 * Link: <a href="https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/">Problem</a>
 * <p>
 * Hint: avoid duplicates existing in banned
 * */

public class Problem2554 {
    public static int maxCount(int[] banned, int n, int maxSum) {
        Arrays.sort(banned);

        long sum = 0;
        int count = 0;
        int i = 0;
        int bl = banned.length;
        for (int j = 1; j <= n; j++) {
            if (j != banned[i]) {
                sum += j;
                if (sum > maxSum) {
                    break;
                }
                count++;
            } else {
                if (i < bl - 1) {
                    i++;
                    // Avoid duplicates
                    while(i < bl - 1 && banned[i] == banned[i-1]) i++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        // 2 and 4; total is 2
        System.out.println(maxCount(new int[]{1, 6, 5}, 3, 6));

        // 0
        System.out.println(maxCount(new int[]{1, 2, 3, 4, 5, 6, 7}, 8, 1));

        // 1, 2, 3, 4, 5, 6, and 7; total is 7
        System.out.println(maxCount(new int[]{11}, 7, 50));


        int[] banned = new int[]{
                87,193,85,55,14,69,26,133,171,180,4,8,29,121,182,78,157,53,26,7,117,138,57,167,
                8,103,32,110,15,190,139,16,49,138,68,69,92,89,140,149,107,104,2,135,193,87,21,
                194,192,9,161,188,73,84,83,31,86,33,138,63,127,73,114,32,66,64,19,175,108,80,176,
                52,124,94,33,55,130,147,39,76,22,112,113,136,100,134,155,40,170,144,37,43,151,137,
                82,127,73
        };
        System.out.println(maxCount(banned, 1079, 87));
    }
}
