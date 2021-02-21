myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def cutYerdeDuranlar(list):
    for i in list:
        if list.index(i)%2==1:
            print(i)
cutYerdeDuranlar(myList)