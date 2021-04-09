def ededler(i):
    coxluq=[]
    for eded in i:
        if eded not in coxluq:
            coxluq.append(eded)
    return coxluq
print(ededler([1,2,3,3,3,3,4,5])) 