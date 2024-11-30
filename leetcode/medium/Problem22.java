package leetcode.medium;


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

    public static List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(n, 0, 0, "", result);
        return result;
    }

    public static void main(String[] args) {
        System.out.println(generateParenthesis(3));
    }
}
