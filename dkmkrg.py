t=int(input())
for tc in range(t):
    a=list(input())
    b=[]
    c,d,e,f,g,h= [],[],[],[],[],[]
    for i in range(len(a)):
        if i=='{':
            c.append(i)
        elif i=='}':
            d.append(i)
        elif i == '(':
            e.append(i)
        elif i == ')':
            f.append(i)
        elif i == '[':
            g.append(i)
        elif i == ']':
            h.append(i)
    if len(c)==len(d) and len(e)==len(f) and len(g)==len(h):
        k=0
        i=0
        while (i<len(c)):
            if (d[i] - c[i])%2 == 0:
                continue
            else:
                print(0)
                k=1
            i+=1
        if k!=1:
            i=0
            while (i<len(f)):
                if (f[i] - e[i]) % 2 == 0:
                    continue
                else:
                    print(0)
                    k = 2
                i += 1
        if k!=1 and k!=2:
            i=0
            while (i<len(h)):
                if (h[i] - g[i]) % 2 == 0:
                    continue
                else:
                    print(0)
                    k=3
                i+=1
        if k==0:
            print(1)
    else:
            print(0)