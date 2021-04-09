bodyStatus=true;
let accBodyElements=document.querySelectorAll('.acc-item-body')
function AccordionFunc(elem){
    for(let i=0;i<accBodyElements.length;i++){
        accBodyElements[i].className='acc-item-body passive'
    }

    let nextElement=elem.nextElementSibling;
    nextElement.className='acc-item-body active' 

    
}
