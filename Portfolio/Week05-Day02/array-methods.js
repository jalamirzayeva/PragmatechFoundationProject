//CONCAT
//2 array yaradaq
let a=[2,4,6,8,10];
let b=[3,5,7,9,11];

// arraylari birlesdirib ad verek
let birlesme=a.concat(b);
//ve consolda arrayin 2 ci elementini gosterek
console.log(birlesme[2])


//copyWithin
let adlar=['Jale','Fatime','Orxan','Ibrahim','Ferid','Eli','Veli','Aydan'];

adlar.copyWithin(1,1,4);

console.log(adlar)


//EVERY
//yaslardan ibaret bir array yaradaq
let yaslar = [12, 26, 46, 30, 55, 17];

function check(yas) {
  return yas >= 18;
}
 let element=yaslar.every(check);
 console.log(element)

//FILL
let numbers=[20,86,25,75,22,34,200,120,33,89,44];
console.log(numbers)
//30 ededini 2-7 araliginde yazdirmaq ucun 
let doldur=numbers.fill(30,2,8)
console.log(doldur)

//FILTER

let ages=[20,11,12,26,86]
function show (age){
    return age <= 18
}
console.log(ages.filter(show))


//FIND
let ededler=[18,11,12,15,25,34,86]
//20 den kicik olanlari tapmaq isteyrem
function goster (tap){
    return tap<20
}
let tapilmalilar=ededler.find(goster);
console.log(tapilmalilar)
// 1-ci 18 i gosterecek cunki arrayda ilk qarsisina cixan eded 18dir


//findIndex
let massiv=[18,33,34,67,70,90,149,665,9,4,1];
//Array elementlerinin index nomrelerini tapmaq istesem
function goster (sira){
    return sira<35
}
let elementnomre=massiv.findIndex(goster)
console.log(elementnomre)