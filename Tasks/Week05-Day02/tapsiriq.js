
    class Car{
        constructor(_Name,_Model,_Price){
            this.Name=_Name
            this.Model=_Model
            this.Price=_Price
              
        }


        showCarDetails(){
            console.log(this.Name + '/' +this.Model + '/' +this.Price)
        }
        checkCarDetails(){
            if(this.Name==Porsche){
                console.log(Car01)
            }else{
                console.log('Melumati duzgun daxil edin')

            }
        }


         
        
    }
            let Car01= new Car('Porsche','718 Cayman T','$62.000')
            let Car02= new Car('BMW','X5','$42.000')
            let Car03= new Car('Mercedes','Benz','$10.000')
            let Car04= new Car('Niva','4*4','$2.000')
            let Car05= new Car('Hyundai','i30','$12.000')
            

            let cars=[
                new Car('Porsche','718 Cayman T','$62.000'),
                new Car('BMW','X5','$42.000'),
                new Car('Mercedes','Benz','$10.000'),
                new Car('Niva','4*4','$2.000'),
                new Car('Hyundai','i30','$12.000')
            ]

           