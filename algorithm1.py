
import math
import random
import sys
import time

sys.setrecursionlimit(20000)

def has_path_dfs(adj, current, target, visited):
    
    if current == target:
        return True
    
    visited.add(current)
    
    for neighbor in adj.get(current, []):
        if neighbor not in visited:
            if has_path_dfs(adj, neighbor, target, visited):
                return True
    
    return False

def run_naive_mst(num_buildings, all_edges):

    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_cost = 0

    adj = {i: [] for i in range(num_buildings)}
    count = 0
    
    for u, v, w in sorted_edges:

        if count == num_buildings - 1:
            break
        
        visited = set()
        if not has_path_dfs(adj, u, v, visited):
            mst_edges.append((u, v, w))
            mst_cost += w
            
            adj[u].append(v)
            adj[v].append(u)
            count += 1
            
    return mst_edges, mst_cost


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
    print("="*30)
    
    test_sizes = [50, 100, 300, 500]
    
    print(f"{'Input Size ':<15} | {'Naive Time ':<15}  ")
    print("-" * 30)
    
    for n in test_sizes:
        edges = generate_data(n)
        
        start = time.time()
        _, cost = run_naive_mst(n, edges)
        end = time.time()
        time0 = end - start

        print(f"{n:<15} | {time0:.6f} ")
        
    print("="*30)
