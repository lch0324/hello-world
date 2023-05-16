A=int(input())
B=(A+4)//6
n=0
while True:
    if (n*(n+1)/2) < B:
        n+=1
    else:
        print(n+1)
        break
