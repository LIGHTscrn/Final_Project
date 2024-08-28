// const button = document.querySelector('button.drop-down-menu');
// const elementToToggle = document.querySelector('.item-hide');

// button.addEventListener('click', () => {
//     elementToToggle.classList.toggle('item-hide');
//     elementToToggle.classList.toggle('item-show');
// });

const button = document.querySelector('.drop-down-menu');
const element = document.querySelector('header');

button.addEventListener('click', () => {
    element.classList.toggle('item-show');
    element.classList.toggle('item-hide');
});