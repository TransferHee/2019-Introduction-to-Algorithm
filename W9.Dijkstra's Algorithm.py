def dijkstra(start, size, weight):
    # Step 1: initialize distance and visited array
    distance = weight[start] 
    visited = [False] * size
    visited[start] = True # mark start vertex as being visited
    
    # Step 2: repeat loop until all vertices are visited
    while(visited!=[True]*size):
        # Step 3: check each vertex for having shortest path
        smallest=float('inf')
        for j in range(len(distance)):
            if(visited[j]==False)and(distance[j]<smallest):
                smallest=distance[j]
                u=j
        visited[u]=True

        # Step 4: for each vertex not in visited array, update its shortest path
        for z in range(len(distance)):
            if visited[z] is False:
                if distance[u]+weight[u][z]<distance[z]:
                    distance[z]=distance[u]+weight[u][z]
    return distance

def d(start,size, weight):
    distance=weight[start]
    visited=[False]*size
    visited[start] = True

    while(visited!=[True]*size):
        smallest=1000000
        for i in range(len(distance)):
            if(visited[i] == False and smallest > distance[i]):
                smallest = distance[i]
                u=i
        visited[u]=True
        for k in range(len(distance)):
            if visited[k] == False:
                distance[k]=min(distance[k], distance[u] + weight[u][k])
    return distance

def s(start,end,size,weight):
    distance=weight[start]
    visited=[False]*size
    visited[start] = True
    x=[[start] for _ in range(size)]
    while(visited!=[True]*size):
        smallest=float('inf')
        for i in range(len(distance)):
            if(visited[i] == False and smallest > distance[i]):
                smallest = distance[i]
                u=i
        x[u].append(u)
        visited[u]=True
        for k in range(len(distance)):
            if visited[k] == False:
                if distance[k] > distance[u]+weight[u][k]:
                    distance[k]=distance[u]+weight[u][k]
                    x[k].append(u)
    print("->".join(map(str,x[end])))
    return distance
def main():
    size = 6

    weight = [
            [0, 2, 5, 1, float('inf'), float('inf')],
            [2, 0, 3, 2, float('inf'), float('inf')],
            [5, 3, 0, 3, 1, 5],
            [1, 2, 3, 0, 1, float('inf')],
            [float('inf'), float('inf'), 1, 1, 0, 2],
            [float('inf'), float('inf'), 5, float('inf'), 2, 0]
    ]

    for i in range(size):
        distance = s(i, 5,size, weight)
    #    print("source = {}".format(i), distance)
    #s(0,4,size,weight)
   
    """
    source = 0 [0, 2, 3, 1, 2, 4]
    source = 1 [2, 0, 3, 2, 3, 5]
    source = 2 [3, 3, 0, 2, 1, 3]
    source = 3 [1, 2, 2, 0, 1, 3]
    source = 4 [2, 3, 1, 1, 0, 2]
    source = 5 [4, 5, 3, 3, 2, 0]
    """

main()
