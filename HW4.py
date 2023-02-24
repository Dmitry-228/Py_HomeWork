def romantoarabic(num):
    numbs = {"1":"I","5":"V","10":"X","50":"L","100":"C"}
    a = 0
    for b,c in enumerate(num):
        if (b+1) == len(num) or numbs[c] >= numbs[num[b+1]]:
            a += numbs[c]
        else:
            a -= numbs[c] 
    return a
while True:
    n = input()
    print(romantoarabic(n))