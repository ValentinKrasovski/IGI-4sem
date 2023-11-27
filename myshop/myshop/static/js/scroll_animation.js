const doorLeft = document.querySelector('#door_left');
const doorRight = document.querySelector('#door_right');
const cloud1 = document.querySelector('#clouds_1');
const cloud2 = document.querySelector('#clouds_2');
const text = document.querySelector('#text');
const man = document.querySelector('#man');

window.addEventListener('scroll',()=>{
    let value = scrollY;
    doorLeft.style.left = `-${value/0.7}px`
    cloud2.style.left = `-${value*2}px`
    doorRight.style.left = `${value/0.7}px`
    cloud1.style.left = `${value*2}px`
    text.style.bottom = `-${value}px`;
    man.style.bottom = `${0 - value*0.5}px`
})