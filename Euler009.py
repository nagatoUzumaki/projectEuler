t = int(input())
lst = []
for _ in range(t):
    lst.append(int(input()))
for n in lst:
    product = -1
    temp = 0
    for a in range(1, (n // 3) + 1):
        b = (n**2 - 2*a*n)//(2*n - 2*a)
        c =  n - a - b
        if (c**2 == a**2 + b**2):
            temp = a*b*c
            if temp > product:
                product = temp
    print(product)