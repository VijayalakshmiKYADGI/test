import time
import sys
from typing import List

def complex_processing(data: List[int]) -> List[int]:
    """
    Function with high cyclomatic complexity and O(n^2) performance issues.
    Modified version with additional complexity.
    """
    results = []
    cache = {}  # Inefficient caching attempt
    
    # Additional nested loop for more complexity
    for i in range(len(data)):
        for j in range(len(data)): 
            if i != j:
                if data[i] > data[j]:
                    if data[i] % 2 == 0:
                        if data[j] % 2 != 0:
                            results.append(data[i] - data[j])
                            cache[f"{i}-{j}"] = data[i] - data[j]  # Wasteful caching
                        else:
                            results.append(data[i] + data[j])
                            cache[f"{i}-{j}"] = data[i] + data[j]
                    else:
                        if data[j] > 5 and data[j] < 100:
                            time.sleep(0.1) # Intentional slow-down
                            results.append(data[i] * data[j])
                            # Additional unnecessary check
                            if sys.getsizeof(results) > 1000:
                                print("Warning: results getting large")
                elif data[i] == data[j]:
                    if i > 0:
                        results.append(0)
                        results.append(0)
                        
    return results

def inefficient_sort(data: List[int]) -> List[int]:
    """
    Bubble sort implementation - O(n^2) sorting algorithm
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                time.sleep(0.01)  # Making it even slower!
    return data
