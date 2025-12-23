
import math
import random
import time

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True 
        
        return False 

def run_optimized_mst(num_buildings, all_edges):

    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_cost = 0
    uf = UnionFind(num_buildings)
    count = 0
    
    for u, v, w in sorted_edges:
        if count == num_buildings - 1:
            break
            
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            mst_cost += w
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
    
    print(f"{'Input Size ':<15} | {'Optimized Time ':<15}")
    print("-" * 30)
    
    for n in test_sizes:
        edges = generate_data(n)
        
        start = time.time()
        _, cost = run_optimized_mst(n, edges)
        end = time.time()
        time0 = end - start
        
        print(f"{n:<15} | {time0:.6f}")
        
    print("="*30)
