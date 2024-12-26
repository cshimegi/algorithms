package leetcode.medium;


import java.util.*;

/**
 * Leetcode 2471
 * <p>
 * Link: <a href="https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/">Problem</a>
 * <p>
 * Hint:
 * */
public class Problem2471 {
    private static class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
    }

    private static int indexOf(int[] arr, int value) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == value) {
                return i;
            }
        }
        return -1;
    }

    private static int countMinSwap(int[] level) {
        int[] temp = Arrays.copyOf(level, level.length);
        Arrays.sort(temp);

        int ans = 0;
        for (int i = 0; i < level.length; i++) {
            if (level[i] != temp[i]) {
                ans++;
                int tmp = level[i];
                int j = indexOf(level, temp[i]);
                level[i] = level[j];
                level[j] = tmp;
            }
        }
        return ans;
    }

    private static int optimizedCountMinSwap(int[] level) {
        int n = level.length;
        int[] sorted = Arrays.copyOf(level, n);
        Arrays.sort(sorted);

        // Map value -> index in the original array
        Map<Integer, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            indexMap.put(level[i], i);
        }

        boolean[] visited = new boolean[n];
        int swaps = 0;

        for (int i = 0; i < n; i++) {
            // Skip if already visited or already in the correct position
            if (visited[i] || level[i] == sorted[i]) {
                continue;
            }

            int cycleSize = 0;
            int current = i;
            // Follow the cycle
            while (!visited[current]) {
                visited[current] = true;
                current = indexMap.get(sorted[current]);
                cycleSize++;
            }

            if (cycleSize > 1) {
                // -1 because a cycle with n nodes has n-1 swaps
                swaps += (cycleSize - 1);
            }
        }

        return swaps;
    }

    public static int minimumOperations(TreeNode root) {
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);

        int ans = 0;
        // Dequeue the nodes in level order
        while (!q.isEmpty()) {
            int levelSize = q.size(); // Number of nodes in the current level
            int[] level = new int[levelSize];
            int k = 0;

            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = q.poll();
                level[k++] = curr.val;

                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            ans += optimizedCountMinSwap(level);
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(minimumOperations(new TreeNode(1, new TreeNode(3), new TreeNode(2, new TreeNode(4), new TreeNode(5)))));
    }
}
