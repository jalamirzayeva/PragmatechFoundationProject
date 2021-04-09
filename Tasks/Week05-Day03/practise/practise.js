class User{
    constructor(_ad,_soyad){
        this.Ad=_ad;
        this.Soyad=_soyad;
    }

    showUserData(){
        console.log(`${this.Ad} | ${this.Soyad}`)
    }
}

// istifadeciden melumatlari almaq
function melumatlariAl(){
    let ad=prompt('Adinizi daxil edin')
    let soyad=prompt('Soyadiniz daxil edin')
    
    return [ad,soyad]
}
// alinan melumatlara esasen obyekt yaratmaq

function obyektYarat(){
    let istifadeciMelumatlari=melumatlariAl()
    user=new User(istifadeciMelumatlari[0],istifadeciMelumatlari[1])

    return user;
}
// elde olunan obyekti arraye elave etmek

function siyahiyaElaveEt(){
    let users=[]
    users.push(obyektYarat())
    return users;
}
// arraydeki obyekt melumatlarini ekrana cap etmek

function melumatlariEkranaCapEt(){
    let usersData=siyahiyaElaveEt()
    for(let i=0;i<usersData.length;i++){
        // usersData[i].showUserData()
        // console.log(usersData[i].Ad)
        // console.log(usersData[i].Soyad)

        console.log(`${usersData[i].Ad} | ${usersData[i].Soyad}`)
    }
}

ededler=[1,3,4,90,23,890,12,30,4,3,67,21]
let ikiReqemlileriSay=0;
for(let i=0;i<ededler.length;i++){
    if(String(ededler[i]).length==2){
        ikiReqemlileriSay++
    }
}
console.log(ikiReqemlileriSay)
