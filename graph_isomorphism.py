def degreeIn(graph, vertex):
    return [graph[i][vertex] for i in range(len(graph))].count(1)

def degreeOut(graph, vertex):
    return graph[vertex].count(1)

def check(A, B):
    if len(A) != len(B):
        return False

    vcount = len(A)
    isoMap = [None] * vcount
    used = [False] * vcount

    isIsm = False

    def findIsomorphism(v1):
        if v1 >= vcount:
            return True

        isCanMap = True

        for v2 in range(vcount):
            if not used[v2] and degreeIn(A, v1) == degreeIn(B, v2) and degreeOut(A, v1) == degreeOut(B, v2):
                isCanMap = True
                for i in range(v1):
                    if A[i][v1] != B[isoMap[i]][v2] or A[v1][i] != B[v2][isoMap[i]]:
                        isCanMap = False
                        break

                if isCanMap:
                    used[v2] = True
                    isoMap[v1] = v2
                    isIsm = findIsomorphism(v1 + 1)
                    if isIsm: return isIsm
                    used[v2] = False
        
        return False

    isIsm = findIsomorphism(0)
    return isIsm

def main():
    n = int(input())

    A = []
    for i in range(n):
        A.append([int(x) for x in input()])

    m = int(input())
    B = []
    for i in range(m):
        B.append([int(x) for x in input()])

    print(check(A, B))

main()
