package leetcode.java.medium;


/**
 * Leetcode 2337
 * <p>
 * Link: <a href="https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/">Problem</a>
 * <p>
 * Hint: Ignore '_' and keep in mind that L can only move to the left and R can only move to the right
 * */

public class Problem2337 {
    public static boolean canChange(String start, String target) {
        int n = start.length();
        int i = 0;
        int j = 0;
        while (i < n || j < n) {
            // Ignore '_'
            while(i < n && start.charAt(i) == '_') i++;
            while(j < n && target.charAt(j) == '_') j++;
            // Check if both reach the end when any of them reaches the end
            if (i == n || j == n) return i == n && j == n;

            // Because L can only move to the left and R can only move to the right,
            // both shown characters should be the same order whatever the positions are
            // when it's movable
            if (start.charAt(i) != target.charAt(j)) {
                return false;
            }
            // L can only move to the left, so the case is impossible when i < j
            else if (start.charAt(i) == 'L' && i < j) {
                return false;
            }
            // R can only move to the right, so the case is impossible when i > j
            else if (start.charAt(i) == 'R' && i > j) {
                return false;
            }
            i++;
            j++;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(canChange("_L__R__R_", "L______RR")); // true
        System.out.println(canChange("R_L_", "__LR")); // false
        System.out.println(canChange("_R", "R_")); // false
    }
}
