
import time
import random
import math

from algorithm1 import run_naive_mst
from algorithm2 import run_optimized_mst

def generate_data(num_buildings):

    buildings = []
    for _ in range(num_buildings):
        buildings.append((random.randint(0, 1000), random.randint(0, 1000)))
    
    edges = []
    for i in range(num_buildings):
        for j in range(i + 1, num_buildings):
            x1, y1 = buildings[i]
            x2, y2 = buildings[j]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            edges.append((i, j, dist))
    return edges

if __name__ == "__main__":
    print("="*65)
    print("MST Algorithm Comparison: Empirical Analysis")
    print("="*65)
    
    test_sizes = [50, 100, 300, 500]
    
    print(f"{'Input Size ':<15} | {'Naive Time ':<15}   | {'Optimized Time ':<20}")
    print("-" * 60)
    
    for n in test_sizes:
        edges = generate_data(n)
        
        start1 = time.time()
        _, cost1 = run_naive_mst(n, edges)
        end1 = time.time()
        time1 = end1 - start1
        
        start2 = time.time()
        _, cost2 = run_optimized_mst(n, edges)
        end2 = time.time()
        time2 = end2 - start2
        
        print(f"{n:<15} | {time1:.6f}          | {time2:.6f}")
        
        if int(cost1) != int(cost2):
            print("  >> WARNING: Costs do not match!")

    print("="*65)
