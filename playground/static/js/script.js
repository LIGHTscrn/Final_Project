document.addEventListener('DOMContentLoaded', () => {
    const icon = document.getElementsByClassName('drop-down-icon')[0];
    const dropDown = document.getElementsByClassName('drop-down-content')[0];
    
    icon.addEventListener('click', () => {
        dropDown.classList.toggle('show');
        dropDown.classList.toggle('fade-in');
    });
});


