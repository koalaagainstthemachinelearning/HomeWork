n=int(input())
for _ in range(n):
    inp=input()
    if len(inp)>10:
        res=inp[0]+str((len(inp))-2)+inp[-1]
        print(res)
    else:
        print(inp)