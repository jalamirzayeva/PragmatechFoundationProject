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


 