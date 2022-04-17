tc = int(input())
for t in range(1, tc + 1):
    d = int(input())
    a=set(int(i) for i in input().split(' '))
    b =set(int(i) for i in input().split(' '))
    print(len(a.intersection(b)))