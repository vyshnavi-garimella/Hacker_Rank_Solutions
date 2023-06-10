n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    ip=input().split()
    if ip[0]=="pop":
        s.pop()
    elif ip[0]=="remove":
        s.remove(int(ip[1]))
    else:
        s.discard(int(ip[1]))
print(sum(s))