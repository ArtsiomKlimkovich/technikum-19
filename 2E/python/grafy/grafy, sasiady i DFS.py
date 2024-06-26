D = {}

n, m = map (int, input().split ())

for i in range(n):
    D[i + 1] = []
    # D.update({ i+1 : [] })

for _ in range(m):
    p, q = map(int, input().split())
    D[p].append(q)
    D[q].append(p)
print(D)

for i in range(1, n + 1):
    if len(D[i]) == 0:
        print("Wiewiór sam")
    else:
        D[i].sort()
        for j in range (len (D[i])):
            print(D[i][j], end=" ")
        print ()

sum = 0
for i in range (1, n + 1):
    sum += len (D[i])

# policz sumę stopni wierzechołków grafu
print (f"suma wierzcholkow grafu: {sum}")

# znajdź wierzchołek o najwyższym stopniu
max = 0
wierzcholek = 0
for i in range (1, n + 1):
    if (max < len (D[i])):
        max = len (D[i])
        wierzcholek = i
print (f"wierzcholek o najwyzszym stopniu: {wierzcholek}")

# znajdź wierzchołki samodzielne
print ("Wierzcholki samodzielne: ", end = "")
for i in range (1, n + 1):
    if (len(D[i]) == 0):
        print (i, end = " ")
print ()
# Sprawdź czy uda się dojść z wierzchołka x do y
x, y = map (int, input().split())
def DFS (D, node, visited): # node to x
    visited.add (node)
    for neighbor in D[node]:
        if neighbor not in visited:
            DFS (D, neighbor, visited)
    return visited

visited = set()
W = DFS (D, x, visited)
if y in W:
    print (f"Istnieje sciezka miedzy {x} i {y}")
else:
    print (f"Nie istnieje sciezki miedzy {x} i {y}")