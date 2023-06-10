n=int(input())
N=set(map(int, input().split()))
b=int(input())
B=set(map(int, input().split()))
x=N.symmetric_difference(B)
z=sorted(x)
for i in z:
    print(i)