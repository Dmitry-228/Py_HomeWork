k = int(input())#ввод значение
m = int(input())#ввод значение
n = int(input())#ввод значение
if n<=k:#условие ЕСЛИ
    t=2*m #
    print(t) 
elif n*2%k ==0: 
    t=m*(n*2//k)
    print(t) 
else: 
    t=m*(1+(n*2//k))
    print(t) 