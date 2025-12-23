

FUNCTION HasPathDFS(Graph, CurrentNode, TargetNode, VisitedSet):
    IF CurrentNode == TargetNode:
        RETURN True
    
    Add CurrentNode to VisitedSet
    
    FOR EACH Neighbor in Graph[CurrentNode]:
        IF Neighbor is NOT in VisitedSet:
            IF HasPathDFS(Graph, Neighbor, TargetNode, VisitedSet):
                RETURN True
    
    RETURN False
    

FUNCTION NaiveMST(Vertices, Edges):
    // Step 1: Sort all edges in non-decreasing order of their weight
    Sort Edges by weight ascending
    
    MST_List = Empty List
    Current_Graph = Empty Adjacency List
    Edge_Count = 0
    
    // Step 2: Iterate through sorted edges
    FOR EACH edge (u, v, weight) in Edges:
        // Optimization: Stop if tree is full
        IF Edge_Count == Vertices - 1:
            BREAK
            
        // Step 3: Cycle Detection using DFS (Naive Step)
        Initialize VisitedSet as Empty
        HasCycle = HasPathDFS(Current_Graph, u, v, VisitedSet)
        
        // If no path exists, it is safe to add the edge
        IF HasCycle is False:
            Add (u, v, weight) to MST_List
            Add v to Current_Graph[u]
            Add u to Current_Graph[v]
            Edge_Count = Edge_Count + 1
            
    RETURN MST_List