for a in range(int(input())):
    n,d = map(int,input().split())
    array = list(map(int,input().split()))
    ans = d  
    for i in range(n-1,-1,-1):
        if d % array[i] != 0 : 
            d = d - (d % array[i] ) 
    print("Case #{}: {}".format(a+1,d))