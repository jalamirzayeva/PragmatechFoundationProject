let sliderImg=document.querySelector('.slider-img');
let img=['slider-1.jpg','slider-2.jpg','slider-3.jpg'];
let i=0; //Current Image Index

function prev(){
    if (i <= 0) i=img.length;
    i--;
    return setImages();
}

function next(){
    if(i>=img.length - 1) i = -1;
    i++;
    return setImages();
}

function setImages(){
    return sliderImg.setAttribute('src','img/'+img[i]);
}