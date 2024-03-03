'''
BFS Practice
James Errington, 2024
'''
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

queue = list()
visited = set()

def bfs(visited, node):
    visited.add(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print (m, end = " ")
        for n in graph[m]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
bfs(visited, '5')
print("")
