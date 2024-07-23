let testimonials = document.getElementsByClassName('testimonial-individual')
let dots = document.getElementsByClassName('dot');
let defaultSlide = 0;

function setEventListeners(){
    for (let i = 0; i < dots.length; i++){
        dots[i].addEventListener('click', (e) => {
            updateSlideNumber(e.target.getAttribute('data-slide'));
        })
    }
}

function setSlidesVisibility(){
    // console.log(testimonials)
    for (let i = 0; i < testimonials.length; i++){
        if (i != defaultSlide) {
            testimonials[i].style.display = 'none';
            dots[i].classList.remove('dot-active');
        } else {
            testimonials[i].style.display = 'flex';
            dots[i].classList.add('dot-active');
        }
    }
}

function updateSlideNumber(slideNum){
    // console.log('inside updateSlideNumber', slideNum);
    defaultSlide = slideNum;
    setSlidesVisibility();
}

setSlidesVisibility();
setEventListeners();
