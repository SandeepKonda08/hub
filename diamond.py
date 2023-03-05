n = int(input())
for i in range(1,n +1):
    lef = " "*(n-i)
    print(lef,end = "")
    for j in range(1,i +1):
        print("*",end = " ")
    print()
for i in range(0,n-1):
    if i == n-2:
        lef1 = " "*(i +1)
        print(lef1 + "*")
    else:
        
        lef = " "* (i +1)
        rig = "  "*(n-i-3)
        print(lef + "* " + rig +"*")
        
