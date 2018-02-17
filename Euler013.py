t = int(input())
lst = []
for _ in range (t):
    lst.append(int(input()))
num = sum(lst)
num = str(num)
print(num[:15])