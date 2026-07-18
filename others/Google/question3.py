"""
file log format: <log id>, <timestamp>, <Start/End>
ID 1, 0, Start
ID 2, 1, Start
ID 3, 2, Start
ID 1, 3, End
ID 4, 5, Start
ID 2, 6, End
...
{3: "ID1", 4: "ID2"}

timeout = 3

Implement a function to know if there is an ID taking too long as soon as possible
"""
from typing import List

def detect_timeout1(logs: List[str], timeout: int) -> bool:
    # Time complexity: O(n) / Space complexity: O(m)
    hashMap = {}
    for line in logs:
        log = line.strip().replace(" ", "").split(",")
        timestamp = int(log[1])
        if log[2] == "Start":
            hashMap[log[0]] = timestamp
        else:
            # End
            startTimestamp = hashMap[log[0]]
            del hashMap[log[0]]
            if timestamp - startTimestamp > timeout:
                return True
    return False

def detect_timeout2(logs: List[str], timeout: int) -> bool:
    # Time complexity: O(n*log(n)) / Space complexity: O(n)
    stack = []
    valid_end_list = set()

    def check_timeout(current_timestamp: int) -> bool:
        l, r = 0, len(stack) - 1
        while l < r:
            mid = (l + r) // 2
            if stack[mid][1] >= current_timestamp - timeout:
                r = mid - 1
            else:
                l = mid + 1
        return stack[l][0] not in valid_end_list and current_timestamp - stack[l][1] > timeout

    for line in logs:
        log = line.strip().replace(" ", "").split(",")
        timestamp = int(log[1])
        if log[2] == "Start":
            stack.append((log[0], timestamp))

        if timestamp - timeout >= 0 and check_timeout(timestamp):
            return True

        if log[2] == "End":
            valid_end_list.add(log[0])

    return False

def detect_timeout1_optimized(logs: List[str], timeout: int) -> bool:
    # Time complexity: O(n) / Space complexity: O(m)
    hashMap = {}
    min_start_time = float('inf')  # Initialize to infinity

    for line in logs:
        log = line.strip().replace(" ", "").split(",")
        operation_id = log[0]
        timestamp = int(log[1])
        event_type = log[2]

        if event_type == "Start":
            hashMap[operation_id] = timestamp
            min_start_time = min(min_start_time, timestamp)  # Update min start time
        else:  # End event
            if operation_id in hashMap:
                start_timestamp = hashMap.pop(operation_id)
                if timestamp - start_timestamp > timeout:
                    return True
            if not hashMap:
                min_start_time = float('inf')
            else:
                min_start_time = min(hashMap.values())

        # Check for timeouts only when necessary
        if timestamp > min_start_time + timeout:
            for active_id, start_time in hashMap.items():
                if timestamp - start_time > timeout:
                    print(line)
                    return True
            if hashMap:
                min_start_time = min(hashMap.values())
            else:
                min_start_time = float('inf')

    return False

def detect_timeout2_optimized(logs: List[str], timeout: int) -> bool:
    # Time complexity: O(n) / Space complexity: O(n)
    records = {}

    for line in logs:
        log = line.strip().replace(" ", "").split(",")
        operation_id = log[0]
        timestamp = int(log[1])
        event_type = log[2]

        if event_type == "Start":
            records[operation_id] = timestamp
        elif event_type == "End":
            if operation_id in records:
                start_timestamp = records.pop(operation_id)
                if timestamp - start_timestamp > timeout:
                    return True

        # Check for timeouts among active operations
        for log_id, start_timestamp in records.items():
            if timestamp - start_timestamp > timeout:
                print("logId:", log_id)
                return True

    return False

if __name__ == "__main__":
    logs = [
        "ID 1, 0, Start",
        "ID 2, 1, Start",
        "ID 1, 2, End",
        "ID 3, 3, Start",
        "ID 2, 4, End",
        "ID 4, 5, Start",
        "ID 3, 6, End",
        "ID 5, 7, Start",
        "ID 5, 8, End",
        "ID 6, 9, Start",
        "ID 4, 10, End",
        "ID 7, 11, Start",
        "ID 6, 12, End",
        "ID 8, 13, Start",
        "ID 7, 14, End",
        "ID 8, 15, End",
    ]
    timeout = 3

    # print(detect_timeout1(logs, timeout))
    # print(detect_timeout2(logs, timeout))
    # print(detect_timeout1_optimized(logs, timeout))
    print(detect_timeout2_optimized(logs, timeout))

