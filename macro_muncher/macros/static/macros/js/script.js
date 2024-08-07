document.addEventListener('DOMContentLoaded', function(){
    let dec = document.querySelector('.weight-input-decrement');
    let inc = document.querySelector('.weight-input-increment');
    let weight = document.querySelector('.weight-input');

    dec.style.width = inc.offsetWidth.toString() + 'px';

    dec.addEventListener('click', () => {
        weight.value >= 1 ? weight.value-- : weight.value
    })

    inc.addEventListener('click', () => {
        weight.value++;
    })
})
