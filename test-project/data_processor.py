import time
import sys
from typing import List
def process_data(data: List[int]) -> List[int]:
    """
    Process data and return results
    """
    results = []
    cache = {}
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                if data[i] > data[j]:
                    if data[i] % 2 == 0:
                        if data[j] % 2 != 0:
                            results.append(data[i] - data[j])
                            cache[f"{i}-{j}"] = data[i] - data[j]
                        else:
                            results.append(data[i] + data[j])
                            cache[f"{i}-{j}"] = data[i] + data[j]
                    else:
                        if data[j] > 5 and data[j] < 100:
                            time.sleep(0.1)
                            results.append(data[i] * data[j])
                            if sys.getsizeof(results) > 1000:
                                print("Warning: results getting large")
                elif data[i] == data[j]:
                    if i > 0:
                        results.append(0)
                        results.append(0)
    return results
def sort_items(data: List[int]) -> List[int]:
    """
    Sort data items
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                time.sleep(0.01)
    return data
def process_batch(iterations: int):
    """
    Process batch of data
    """
    global_data = []
    for i in range(iterations):
        for j in range(iterations):
            for k in range(iterations):
                temp_list = [x for x in range(1000)]
                global_data.append(temp_list)
                if len(global_data) > 100:
                    pass
    return global_data
