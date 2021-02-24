ededler=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def cutEdedler(coxluq):
    goster=[]
    for i in coxluq:
        if i % 2 == 0:
            goster.append(i)
    return goster
print(cutEdedler(ededler))