let section=document.createElement('section')
section.idName='gallery'
document.body.appendChild(section)

let container=document.createElement('div')
container.className='container'

let row=document.createElement('div')
row.className='row'

let col=document.createElement('div')
col.className='col-4'

let box=document.createElement('div')
box.className='box'

let image=document.createElement('img');
let imgindex=1
       

//elementləri yaratdıqdan sonra iç-içə əlavə edirik

box.appendChild(image)
col.appendChild(box)
row.appendChild(col)
container.appendChild(row)
section.appendChild(container)

//elementləri iç-içə əlavə etdikdən sonra for() ilə yaradaq
for(let rowCount=0; rowCount<2;rowCount++ ){
    let row=document.createElement('div')
    row.className='row'

    for(let colCount=0;colCount<3;colCount++){
        let col=document.createElement('div')
        col.className='col-4'

        let box=document.createElement('div')
        box.className='box'

        let image=document.createElement('img')
        image.setAttribute=('src','img/'+imgindex+'.jpg')
        



        box.appendChild(image)
        col.appendChild(box)
        row.appendChild(col)
       
    }
    container.appendChild(row)
}
section.appendChild(container)
