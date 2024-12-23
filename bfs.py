graph = {}
entries= int(input("enter no. of nodes: "))

for i in range(entries):
    key = input("enter node : ")
    value = input(f"enter adjecent nodes for {key} (comma-seperated) : ")

    value_list = value.split(',')
    graph[key] = value_list

print("constructed graph")
print(graph)

visited=[]
queue=[]

def bfs(v,graph,start):
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(f"visted node {node}")
        

        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

start_node = input("enter the start node: ")
bfs(visited,graph,start_node)