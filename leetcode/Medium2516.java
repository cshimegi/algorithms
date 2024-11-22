package leetcode;

import java.util.HashMap;

/**
 * Leetcode 2516
 *
 * Link: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
 *
 * Hint: Invert version of sliding window -> the window is not the target
 * */
public class Medium2516 {
    public static int takeCharacters(String s, int k) {
        // Count the characters
        int[] counters = new int[3];
        for (int i = 0; i < s.length(); i++) {
            counters[s.charAt(i) - 'a']++;
        }

        // Check if any one of the characters is less than k
        if (counters[0] < k || counters[1] < k || counters[2] < k) {
            return -1;
        }

        // Find the minimum length
        int result = s.length();
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            // Exclude the character at the right pointer
            counters[s.charAt(r) - 'a']--;

            while (counters[0] < k || counters[1] < k || counters[2] < k) {
                // Add this to count before moving left pointer 1 step to the right
                counters[s.charAt(l) - 'a']++;
                // Move left pointer 1 step to the right
                l++;
            }

            // Update the result
            int windowSize = r - l + 1;
            result = Math.min(result, s.length() - windowSize);
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(takeCharacters("aabaaaacaabc", 2));
        System.out.println(takeCharacters("aaaaaaaaa", 3));
    }
}
