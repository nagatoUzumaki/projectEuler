t = int(input())
lst = []
for i in range(t):
    n = int(input())
    lst.append(n)
nlst = []
for n in lst:
    for i in range(100,1000):
        for j in range(100,1000):
            pel = i * j
            if pel >= 101101:
                nlst.append(pel)
                spel = str(pel)
                ln = len(spel)
                for k in range(ln//2):
                    if(spel[k] != spel[ln-1-k]):
                       break
                else:
                    nlst.remove(pel)
    print(nlst)
'''
len = s.length();
for (int
i = 0;
i < len / 2;
i + +){
if (s.charAt(i) != s.charAt(len - 1 - i))
return 0;
}
return 1;
}


a[] = new
int[1000001];
int
k = 0, count = 0;

for (int i=100;i <= 999;i++){
for (int j=100;j <= 999;j++){
int pro=i * j;
if (pro >= 101101){
int val=check(""+pro);
if (val == 1)a[pro]=1;
}
else a[pro]=0;
}
}
int
t = in.nextInt();
for (int a0 = 0; a0 < t; a0++){
int n = in.nextInt();
for (int i=n-1;i >= 101101;i--){

if (a[i] == 1){
System.out.println(i);
break;
}
}
}
}'''