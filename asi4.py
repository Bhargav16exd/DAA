def dijikstra(graph,k):
    
    length = len(graph)

    distance = [1000] * length
    visited = [False] * length

    #Starting Index is zero from itself
    distance[k-1] = 0 

    # N number of nodes are to be visited but any order so we loop N times

    for _ in range(length):

        u = -1
        minDistance = 1000

        #We loop to find min dist node and mark them as visited
        for i in range(length):
            if visited[i] != True and minDistance > distance[i]:
                u = i 
                minDistance = distance[i]

    

        if u == -1 :
            break

        visited[u] = True

        #Update Nearby Nodes Value , V represent J and loops through each element in row 
        for v in range(length):
            if visited[v] != True and graph[u][v] != 1000:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]



    print(f"Shortest distances from node {k}:")
    for i in range(n):
        if distance[i] == 1000:
            print(f"Node {i}: Not reachable")
        else:
            print(f"Node {i}: {distance[i]}")


#Main 
n = int(input("Enter Number of Nodes "))
k = int(input("Enter Source Vertex : "))

graph = []

for i in range(n):
    row = []
    for j in range(n):
        weight = int(input(f"Enter Weight Corresponding to {i , j} : "))
        row.append(weight)
    graph.append(row)

dijikstra(graph,k)