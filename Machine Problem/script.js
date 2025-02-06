
function showBox(day, color) {
    const bigBoxContainer = document.getElementById('bigBoxContainer');
    const bigBox = bigBoxContainer.querySelector('.bigBox');
    
    bigBox.textContent = day;
    bigBox.style.backgroundColor = color;

    
    bigBoxContainer.classList.remove('visible');

    
    void bigBoxContainer.offsetWidth; 


    bigBoxContainer.classList.add('visible');
}


document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.sidebar button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const day = button.textContent;
            const color = button.getAttribute('data-color');
            showBox(day, color);
        });
    });
});
