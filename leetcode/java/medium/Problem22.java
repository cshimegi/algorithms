package leetcode.java.medium;


import java.util.List;
import java.util.ArrayList;


/**
 * Leetcode 22
 * <p>
 * Link: <a href="https://leetcode.com/problems/generate-parentheses/description/">Problem</a>
 * <p>
 * Hint: Backtrack
 * */
public class Problem22 {
    private static void backtrack(int n, int open, int close, String current, List<String> result) {
        if (current.length() == n*2) {
            result.add(current);
            return;
        }

        if (open < n) {
            backtrack(n, open+1, close, current + "(", result);
        }

        if (close < open) {
            backtrack(n, open, close+1, current + ")", result);
        }
    }

    /**
     * Do backtrack with dynamic programming
     * i    dp[i]
     * 0	[""]
     * 1	["()"]
     * 2	["()()", "(())"]
     * 3	["()()()", "()(())", "(())()", "(()())", "((()))"]
     * Hint: dp[i] is the combination of `"(" + dp[j] ")" + dp[i-j-1]` where 0 <= j < i and 1 <= i <= n
     * */
    private static List<String> dpBacktrack(int n) {
        List<List<String>> dp = new ArrayList<>();
        // Initialization
        dp.add(new ArrayList<>());
        dp.get(0).add("");

        // Build dp[i] for 1 to n pairs
        for (int i = 1; i <= n; i++) {
            List<String> current = new ArrayList<>();
            for (int j = 0; j < i; j++) {
                List<String> left = dp.get(j);
                List<String> right = dp.get(i-j-1);
                for (String l : left) {
                    for (String r : right) {
                        current.add("(" + l + ")" + r);
                    }
                }
            }
            dp.add(current);
        }

        return dp.get(n);
    }

    public static List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(n, 0, 0, "", result);
        return result;
    }

    public static void main(String[] args) {
        System.out.println(generateParenthesis(3));

        System.out.println(dpBacktrack(3));
    }
}
