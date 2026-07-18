"""
|----- 1000 -----|----- 1000 -----| Capacity = 1000
|----------- 1600 -----------| DataSize = 1600
|---- 800 ----|---- 800 ----| SplitPackets = {800, 800}


|-100-|---- 900 ----|----- 1000 -----| Capacity = 1000, headerSize = 100
|-100-|--------- 1600 -----------| DataSize = 1600
|-100-|---- 750 ----|---- 850 ----| SplitPackets = {750, 850}
"""
from typing import List

def split_data(data_size: int, capacity: int) -> List[int]:
    pass

def split_data2(data_size: int, capacity: int, header_size: int) -> List[int]:
    pass


if __name__ == "__main__":
    pass

