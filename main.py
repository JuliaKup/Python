import numpy as np

def degree(vertex):
    return vertex.count(1)

def check(A, B, AIsms = None):
    if len(A) != len(B):
        return False

    vcount = len(A)
    isoMap = []

    if AIsms: AIsms = [[] for _ in range(vcount)]

    used = [False] * vcount
    deg1 = [degree(v) for v in A]
    deg2 = [degree(v) for v in B]

    isIsm = False

    v2 = 0

    def findIsomorphism(v):
        if v >= vcount:
            isIsm = True
            if AIsms: AIsms.append(isoMap)
        else:
            return

        for v2 in range(vcount):
            if not used[v2] and deg1[v1] == deg2[v2]:
        isCanMap = True
        if isCanMap:
            used[v2] = True
            isoMap[v1] = v2
            findIsomorphism(v1 + 1)
            if isIsm and ...: return isIsm
            used[v2] = False
        pass

    return isIsm

def main():
    n = int(input())

    A = []
    for i in range(n):
        A.append([int(x) for x in input().split()])

    m = int(input())
    B = []
    for i in range(m):
        B.append([int(x) for x in input().split()])

    return check(A, B)

main()