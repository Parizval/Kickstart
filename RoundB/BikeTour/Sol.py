for a in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    ans = 0 
    for i in range(1,n-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            ans +=1 
    print("Case #{}: {}".format(a+1,ans))