T = int(input())
for i in range(T):
    n = input()
    l = len(n)
    if l % 2 == 0:#if it is even number then b and c variables will split in two equal parts
        b, c = n[:l//2], n[l//2:]
    else:#if it is odd number then b and c variables will split in two equal parts leaving the middle element
        b, c = n[:l//2], n[l//2+1:]
    if sorted(b) == sorted(c):#check if the splitted parts are epual or not
        print("YES")
    else:
        print("NO")