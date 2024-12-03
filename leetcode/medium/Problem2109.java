package leetcode.medium;


/**
 * Leetcode 2109
 * <p>
 * Link: <a href="https://leetcode.com/problems/adding-spaces-to-a-string/description/">Problem</a>
 * <p>
 * Hint:
 * */
public class Problem2109 {
    public static String addSpaces(String s, int[] spaces) {
        StringBuilder sb = new StringBuilder();
        int total = spaces.length;
        int index = 0;
        for (int i = 0; i < s.length(); i++) {
            if (index < total && i == spaces[index]) {
                sb.append(" ");
                index++;
            }
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String actual1 = addSpaces("LeetcodeHelpsMeLearn", new int[]{8, 13, 15});
        String expect1 = "Leetcode Helps Me Learn";
        System.out.println(actual1.equals(expect1)); // true

        String actual2 = addSpaces("icodeinpython", new int[]{1, 5, 7, 9});
        String expect2 = "i code in py thon";
        System.out.println(actual2.equals(expect2)); // true

        String actual3 = addSpaces("spacing", new int[]{0, 1, 2, 3, 4, 5, 6});
        String expect3 = " s p a c i n g";
        System.out.println(actual3.equals(expect3)); // true

        String actual4 = addSpaces("apple", new int[]{});
        String expect4 = "apple";
        System.out.println(actual4.equals(expect4)); // true
    }
}
