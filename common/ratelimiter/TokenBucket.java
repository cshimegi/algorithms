package common.ratelimiter;

import java.util.concurrent.locks.ReentrantLock;

public class TokenBucket {
    private static class RateLimiter {
        private final long rate; // refill rate in tokens per second
        private final long capacity; // maximum number of tokens
        private long tokens; // current available tokens
        private long lastRefillTimestamp;
        private final ReentrantLock lock = new ReentrantLock();


        public RateLimiter(long rate, long capacity) {
            this.rate = rate;
            this.capacity = capacity;
            this.tokens = capacity;
            this.lastRefillTimestamp = System.currentTimeMillis();
        }

        public boolean acquire() {
            lock.lock();

            try {
                refill();
                if (tokens > 0) {
                    tokens--;
                    return true;
                }
            } finally {
                lock.unlock();
            }

            return false;
        }

        private void refill() {
            long now = System.currentTimeMillis();
            long elapsed = now - lastRefillTimestamp;
            if (elapsed > 0) {
                tokens += elapsed * rate / 1000;
                if (tokens >= 1) {
                    tokens = Math.min(tokens, capacity);
                    lastRefillTimestamp = now;
                }
            }
        }
    }


    public static void main(String[] args) {
        RateLimiter rateLimiter = new RateLimiter(2, 5);
        
        for (int i = 1; i <= 1; i++) {
            final int writeId = i;
            new Thread(() -> {
                while (true) {
                    if (!rateLimiter.acquire()) {
                        continue;
                    }
                    try {
                        System.out.println("Thread " + writeId + " acquired a token.");
                        System.out.println("Current time: " + System.currentTimeMillis());
                        Thread.sleep(200); // Simulate some work with the token
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        throw new RuntimeException("Thread interrupted during processing", e);
                    }
                }
            }).start();
        }
    }
}
