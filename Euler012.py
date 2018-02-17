import math
t = int(input())
lst = []
for _ in range(t):
    lst.append(int(input()))
tn = []
num = 0
temp = 0
for i in range(1001):
    while(temp <= i):
        num += 1
        tno = num * (num + 1) // 2
        count = 0
        for j in range(1,math.ceil(math.sqrt(tno))):
            if(tno % j == 0):
                count += 2
                print(count)
        if (math.ceil(math.sqrt(tno)) == math.floor(math.sqrt(tno))):
            count += 1
        temp = count
        print(temp)
        tn.append(tno)
for n in tn:
    print(tn[n])

