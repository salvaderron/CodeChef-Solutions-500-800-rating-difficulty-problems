# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if (abs(b-a)%2)==0:
        print("Yes")
    else:
        print("No")
