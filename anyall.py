N=int(input())
a=list(map(int,input().split()))
print([False,any(map(lambda x: str(x) == str(x)[::-1], a))][all(map(lambda x: x>0, a))])
