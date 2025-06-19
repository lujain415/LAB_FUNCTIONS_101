def h(n):
    p=""
    for i in range(n,0,-1):
        for j in range(i,0,-1):
             p += str(j) + " "
        p +=("\n")
    return p
k=h(8)
print(k)