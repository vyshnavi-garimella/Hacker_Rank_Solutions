cube = lambda x: pow(x,3)
# complete the lambda function 

def fibonacci(n):
    z = [0,1]
    for i in range(2,n):
        z.append(z[i-2]+z[i-1])
    return(z[0:n]) # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))