myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def tekrarEdedler(list):
    goster=[]
    for i in list:
        a=list.count(i)
        if a>1:
            if goster.count(i)!=1:
                goster.append(i)
    return goster
print(tekrarEdedler(myList))