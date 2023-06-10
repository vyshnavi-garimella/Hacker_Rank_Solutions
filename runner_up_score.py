if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=set(arr)
    res=sorted(s)
    r=list(res)
    print(r[-2])