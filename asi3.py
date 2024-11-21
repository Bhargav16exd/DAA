def floyddWarshall(graph,dist):
    
    length = len(graph)

    #Initializing Distance Matrix
    for i in range(length):
        for j in range(length):
            if i == j :
                dist[i][j] = 0
            elif graph[i][j] != -1 :
                dist[i][j] = graph[i][j]

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] =  dist[i][k] + dist[k][j]
            
    return dist


#Main Code 
n = int(input("Enter Number of Offices: "))
print("Enter Adjacency Matrix")

# Init Graph and dist matrix to inf
graph = []
dist  = []

for i in range(n):
    row  = []
    row1 = []
    for j in range(n):
        num =  input(f"Enter Distance between Office {i + 1} and Office {j + 1} :")
        row.append(int(num))
        row1.append(float('inf'))
    
    graph.append(row)
    dist.append(row1)

result = floyddWarshall(graph,dist)

for i in range(n):
    for j in range(n):
        print(f"{result[i][j]} " , end=" ")
    print(end="\n")