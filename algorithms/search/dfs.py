'''
DFS Practice
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

def dfs(visited, node):
    visited.add(node)
    queue.append(node)

    while queue:
        m = queue.pop()
        print (m, end = " ")
        for n in graph[m]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
dfs(visited, '5')
print("")
