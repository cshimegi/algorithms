package leetcode.medium;


/**
 * Leetcode 1930
 * <p>
 * Link: <a href="https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/">Problem</a>
 * <p>
 * Hint: Record the visited characters for leftmost and rightmost occurrence and
 *       count unique middle characters of palindromic subsequence
 * */

public class Problem1930 {
    public static int countPalindromicSubsequence(String s) {
        // Record the visited characters for leftmost and rightmost occurrence
        int[] visited = new int[26];
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (visited[s.charAt(i) - 'a'] == 0) {
                visited[s.charAt(i) - 'a'] = 1;
                int lastIndex = s.lastIndexOf(s.charAt(i));
                // Count unique characters to form unique palindromic subsequence
                int[] subVisited = new int[26];
                for (int j = i + 1; j < lastIndex; j++) {
                    if (subVisited[s.charAt(j) - 'a'] == 0) {
                        subVisited[s.charAt(j) - 'a'] = 1;
                        count++;
                    }
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(countPalindromicSubsequence("aabca"));
    }
}
