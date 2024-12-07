package leetcode.medium;


/**
 * Leetcode 29
 * <p>
 * Link: <a href="https://leetcode.com/problems/divide-two-integers/description/">Problem</a>
 * <p>
 * Hint: Utilize bitwise operations to find the largest multiply first and then subtract for better performance
 * */

public class Problem29 {
    public static int divide(int dividend, int divisor) {
        if (dividend == 0) return 0;
        if (dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        if (dividend == Integer.MIN_VALUE && divisor == 1) return Integer.MIN_VALUE;

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long absDividend = Math.abs((long) dividend);
        long absDivisor = Math.abs((long) divisor);

        int res = 0;
        while (absDividend >= absDivisor) {
            long tempDivisor = absDivisor;
            long multiply = 1;
            // Find the largest multiply by shifting for better performance
            while (absDividend >= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiply <<= 1;
            }
            absDividend -= tempDivisor;
            res += multiply;
        }
        return negative ? -res : res;
    }

    public static void main(String[] args) {
        System.out.println(divide(10, 3));
        System.out.println(divide(7, -3));
        System.out.println(divide(-99, -2));
        System.out.println(divide(99, -7));
        System.out.println(divide(-2147483648, -1));
        System.out.println(divide(-2147483648, 2));
        System.out.println(divide(1000000000, 1));
    }
}
