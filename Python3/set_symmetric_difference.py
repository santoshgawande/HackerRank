am = int(input())
a = set(map(int,input().split()))
bm = int(input())
b =set(map(int,input().split()))
print(len(a.symmetric_difference(b)))