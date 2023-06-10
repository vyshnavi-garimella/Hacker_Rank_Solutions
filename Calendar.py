import datetime
x=list(map(int,input().split()))

x=datetime.datetime(x[2],x[0],x[1])
Z=x.strftime("%A")
print(Z.upper())