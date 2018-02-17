t = int(input())
lst = []
for a in range (t):
    n = int(input())
    lst.append(n)
    sum = 0
for n in lst:
    n1 = n // 3
    n1 = 3 * n1 * (n1 + 1) // 2
    n2 = n // 5
    n2 = 5 * n2 * (n2 + 1) // 2
    n3 = n // 15
    n3 = 15 * n3 * (n3 + 1) // 2
    print(n1 + n2 -n3)
