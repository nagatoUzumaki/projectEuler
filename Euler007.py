import math
t = int(input())
lst = []
for _ in range (t):
    lst.append(int(input()))
primes = [2, 3, 5, 7]
j = 9
for n in lst:
    while (n > len(primes)):
        j += 2
        flag = 0
        for k in range(2, int(math.sqrt(j) + 1)):
            if(j % k == 0):
                flag =  1
        if flag == 0:
            primes.append(j)
    print(primes[n - 1])