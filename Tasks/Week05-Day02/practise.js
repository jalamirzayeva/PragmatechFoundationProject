let phones=[]
class Phone {
    //bu obyektde 3 property olacaq
    constructor(_name,_model,_price){
         this.Name=_name
         this.Model=_model
         this.Price=_price
    }
    //Phone obyektinin detallarini gosteren metod yazaq
    showPhoneDetails(){
        let phoneDetails = `${this.Name} | ${this.Model} | ${this.Price}`
        console.log(phoneDetails)
    }
   
}
// 4 eded Phone obyekti yaradaq
let phone01= new Phone('iphone','Xs',1700)
let phone02= new Phone('Samsung','a71',700)
let phone03= new Phone('Xiaomi','Note9',500)
let phone04= new Phone('Huawei','p40',2000)

//bu obyektleri yuxarida yazdigimiz phones arrayine elave edek

phones.push(phone01)
phones.push(phone02)
phones.push(phone03)
phones.push(phone04)

//indi ele funksiya yazaq ki telefon adi yazanda o telefonun butun melumatlarini gore bilek
function showPhoneByName(_phonename){
    for(let i=0; i<phones.length;i++){
        if(phones[i].Name==_phonename){
            phones[i].showPhoneDetails()
        }
    }
}
//ya da deyer yox nese bir telefon modeli axtarmaq istesek,model axtaranda ancaq hemin modelin telefonlarini cixartsin

function showPhoneByModel(_phonemodel){
    for(let i=0; i<phones.length;i++){
        if(phones[i].Model==_phonemodel){
            phones[i].showPhoneDetails()
        }
    }
}

//parametr olaraq nese bir deyer versek, hemin deyerden bahali telefonlari gostersin

function showPhoneByPrice(_phoneorice){
    for(let i=0; i< phones.length;i++){
        if(phones[i].Price>_phoneprice){
            phones[i].showPhoneDetails()
        }
    }
}