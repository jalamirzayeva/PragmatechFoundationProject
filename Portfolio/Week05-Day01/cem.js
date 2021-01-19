// array yaradaq
var ededler=[1,3,4,90,23,890,12,30,4,3,67,21];
 
//arraydaki ededlerin ceminin tapilmasi
var cem=0;
for(var i=0; i<Array.length;i++){
    cem = ededler[i] + cem;
}
console.log(cem)