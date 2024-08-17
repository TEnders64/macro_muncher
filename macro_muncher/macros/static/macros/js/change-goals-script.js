document.addEventListener('DOMContentLoaded', function(){

    weightIncDecButtons();

    pacingToggle();

    changeGoalsStyleIncButton();

});

window.addEventListener('resize', changeGoalsStyleIncButton);

// track weight goal inc/dec buttons
function weightIncDecButtons(){
    let dec = document.querySelector('.change-goals-form .weight-input-decrement');
    let inc = document.querySelector('.change-goals-form .weight-input-increment');
    let weight = document.querySelector('.change-goals-form .goal-weight');

    dec.style.width = inc.offsetWidth.toString() + 'px';

    dec.addEventListener('click', () => {
        weight.value >= 1 ? weight.value-- : weight.value
    })

    inc.addEventListener('click', () => {
        weight.value++;
    })
}

// change goals form disabling pacing for Maintain goal
function pacingToggle(){
    let goal = document.querySelector('.goal-type');
    goal.addEventListener('change', () => {
        let pacing = document.querySelector('.goal-pacing');
        goal.value == 'Maintain' ? pacing.disabled = true : pacing.disabled = false
    });
}

// change goals form inc/dec buttons
function changeGoalsStyleIncButton() {
    let weightInput = document.querySelector('.change-goals-form .goal-weight');
    let dec = document.querySelector('.change-goals-form .weight-input-decrement');
    let offset = weightInput.getBoundingClientRect().left - dec.getBoundingClientRect().left;
    dec.style.left = offset + 'px';
}