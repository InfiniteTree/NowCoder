n = int(input())
nodes = [list(map(int, input().split())) for i in range(n)]
tx, ty = map(int, input().split())
def getResult(nodes, tx, ty):
    if tx < 0 or ty < 0:
        return "{}"
    matrix = []
    dfs(matrix, nodes[0], 0)
    if tx < len(matrix) and ty < len(matrix[tx]):
        return "{" + str(matrix[tx][ty]) + "}"
    else:
        return "{}"
 
def dfs(matrix, node, level):
    if node is None:
        return
    val = node[0]
    if level < len(matrix):
        matrix[level].append(val)
    else:
        matrix.append([val])
    for i in range(1, len(node)):
        child = node[i]
        dfs(matrix, nodes[child], level + 1)
 
print(getResult(nodes, tx, ty))