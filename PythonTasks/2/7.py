def checkString(cumle):
    a={'boyuk-herf':0,'kicik-herf':0}
    for i in cumle:
        if i.isupper():
            a['boyuk-herf']+=1
        elif i.islower():
            a['kicik-herf']+=1
    print(cumle)
    print( 'Boyuk herfler:',a['boyuk-herf'])
    print( 'Kicik herfler:',a['kicik-herf'])
checkString('Meqsedimiz yaxsi Developer olmaqdir')