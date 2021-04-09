userList=[
    {
        name:'Sabir',
        email:'sabir@mail.com',
        userTasks:[
            {
                taskName:'Task01',
                taskDeadline:2
            },
            {
                taskName:'Task02',
                taskDeadline:8
            },
            {
                taskName:'Task03',
                taskDeadline:10
            }

        ]
    },
    {
        name:'Hesen',
        email:'hesen.mail.com',
        userTasks:[
            {
                taskName:'XTask01',
                taskDeadline:2
            },
            {
                taskName:'XTask02',
                taskDeadline:15
            },
            {
                taskName:'XTask03',
                taskDeadline:4
            }

        ]
    }
]
//istifadeci adi daxil etdikde hemin istifadecinin tasklarini gormek ucun:
function findUserTasksByName(userName){

    for(let i=0;i<userList.length ; i++){

        if(userList[i].name==userName){
            console.log( userList[i].userTasks)
        }else{
            console.log('')
        }

    }
} 
findUserTasksByName('Sabir')

 
//Istifadecilerin mailleri daxilinde @ isaresinin olub olmamasini yoxlamaq ucun:
function userEmailCheck(){

    for(let j=0; j<userList.length ; j++){

        if(userList[j].email.indexOf("@")<=0){
            console.log(userList[j].name + ", zehmet olmasa emilinizi duzgun qeyd edin !");
        }else{}

    }
} 
userEmailCheck()

//en uzun deadlinea sahib olan taskin adini muddetini,ve kime aid oldugunu gormek ucun:
function findLongesDeadline(){
  
    for(let k=0; k<10;k++){
        
        if(userTasks[0].taskDeadline<userTasks[1].taskDeadline){
            
            console.log(userTasks[k].taskDeadline +" boyukdur")
        }
    }

}

findLongesDeadline()
