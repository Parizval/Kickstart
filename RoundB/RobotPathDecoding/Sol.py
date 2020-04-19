for a in range(int(input())):
    string = input()
    power = 1 
    w = 1 ; h = 1 
    stact = []
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] == "N":
                h -= power
            elif string[i] == "S":
                h += power
            elif string[i] == "E":
                w += power
            else: 
                w -= power
        elif string[i].isnumeric():
            stact.append(int(string[i]))
            power *= int(string[i])
        elif string[i] == ")":
            power = int(power/stact[-1])
            stact.pop()
        else: 
            continue
    if h < 1 : 
        h =  10**9 - (-h%10**9) 
    if w  < 1 : 
        w  = 10**9 - (-w%10**9)
    print("Case #{}: {} {}".format(a+1,w,h))