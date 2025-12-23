

// Data Structure Definition
STRUCTURE UnionFind:
    Parent Array
    Rank Array

    FUNCTION Initialize(N):
        FOR i from 0 to N-1:
            Parent[i] = i
            Rank[i] = 0

    FUNCTION Find(i):
        // Path Compression: Point node directly to root
        IF Parent[i] != i:
            Parent[i] = Find(Parent[i])
        RETURN Parent[i]

    FUNCTION Union(i, j):
        RootI = Find(i)
        RootJ = Find(j)
        
        IF RootI != RootJ:
            // Union by Rank: Attach smaller tree to larger tree
            IF Rank[RootI] > Rank[RootJ]:
                Parent[RootJ] = RootI
            ELSE IF Rank[RootI] < Rank[RootJ]:
                Parent[RootI] = RootJ
            ELSE:
                Parent[RootJ] = RootI
                Rank[RootI] = Rank[RootI] + 1
            RETURN True  // Successful union (No cycle)
        
        RETURN False // Cycle detected

// Main Algorithm
FUNCTION OptimizedMST(Vertices, Edges):
    // Step 1: Sort all edges in non-decreasing order of their weight
    Sort Edges by weight ascending
    
    MST_List = Empty List
    DSU = Initialize UnionFind(Vertices)
    Edge_Count = 0
    
    // Step 2: Iterate through sorted edges
    FOR EACH edge (u, v, weight) in Edges:
        IF Edge_Count == Vertices - 1:
            BREAK
            
        // Step 3: Cycle Detection using Union-Find (Optimized Step)
        // DSU.Union returns True if nodes were in different sets
        IF DSU.Union(u, v) is True:
            Add (u, v, weight) to MST_List
            Edge_Count = Edge_Count + 1
            
    RETURN MST_List