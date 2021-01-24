let images=['img/1.jpg','img/2.jpg','img/3.jpg','img/4.jpg','img/5.jpg','img/6.jpg','img/7.jpg','img/8.jpg','img/9.jpg'];
let rowContent='';

for(let i=0;i<images.length;i++){
    let colContent=`
                <div class="col-4">
                    <div class="box" onclick='showBigImage(this)'>
                        <img src=${images[i]} alt="">
                    </div>
                </div>
    `
    rowContent+=colContent
}

document.querySelector('.row').innerHTML=rowContent

function showBigImage(element){
    let imgURL=element.querySelector('img').getAttribute('src');
    let overlayContent=`
    
        <div class="overlay" onclick='closeImage()'>
            <img src=${imgURL} alt="">
        </div>
    `
    
    document.querySelector('.row').innerHTML=rowContent+overlayContent
}

function closeImage(){
    document.querySelector('.row').removeChild(document.querySelector('.overlay'))
}