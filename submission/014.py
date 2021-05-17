N = int(input())
A = sorted(list(map(int,input().split())))
N = sorted(list(map(int,input().split())))
print(sum(abs(a-n) for a,n in zip(A,N)))
