def generalizedGCD(num,arr):
    arr.sort()
    i=1
    current=0
    prev=0
    tonext=True
    while i < num:
        current = i*2
        for s in arr:
            if s%current==0 and tonext:
                tonext=True
            else:
                tonext=False
        if tonext:   
            prev = current
        else:
            return prev
        i+=1
    pass
print(generalizedGCD(5,[2,4,6,8]))