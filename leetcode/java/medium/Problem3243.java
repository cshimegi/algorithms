package leetcode.java.medium;

import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Leetcode 3243
 * <p>
 * Link: <a href="https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/">Problem</a>
 * <p>
 * Hint: BFS for each query
 * */
public class Problem3243 {
    private static int bfs(Map<Integer, List<Integer>> graph, int start, int end) {
        // Initialize queue
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        // Initialize distance with MAX_VALUE because we want to find the shortest distance
        int[] distance = new int[end+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;

        // main BFS to visit all nodes
        while (!queue.isEmpty()) {
            int node = queue.poll();
            // Visit all neighbors
            for(int neighbor : graph.getOrDefault(node, new ArrayList<>())) {
                if (distance[neighbor] == Integer.MAX_VALUE) {
                    distance[neighbor] = distance[node] + 1;
                    queue.add(neighbor);
                }
            }
        }
        return distance[end];
    }

    public static int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        // Initialize graph 0 -> 1, 1 -> 2, 2 -> 3, ...
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n-1; i++) {
            graph.putIfAbsent(i, new ArrayList<>());
            graph.get(i).add(i+1);
        }

        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            // Update graph
            graph.get(queries[i][0]).add(queries[i][1]);
            // Find the shortest distance
            result[i] = bfs(graph, 0, n-1);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] results = shortestDistanceAfterQueries(5, new int[][]{{2, 4}, {0, 2}, {0, 4}});
        System.out.println(Arrays.toString(results));

        int[] results2 = shortestDistanceAfterQueries(6, new int[][]{{1, 4}, {0, 2}});
        System.out.println(Arrays.toString(results2));
    }
}
