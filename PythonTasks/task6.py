myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def tekYerdeDuranlar():
    for i in myList:
        if i%2>0:
            myList.remove(i)
    for i in myList:
        print(i)
tekYerdeDuranlar()