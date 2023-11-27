const contact_one_all = document.querySelectorAll('.contact_one');

for (let i = 0; i < contact_one_all.length; i++) {
    const contact_i = contact_one_all[i];
    contact_i.addEventListener('mousemove', function (event) {
        rotate(event, contact_i);
    });

    contact_i.addEventListener('mouseout', function (event) {
        stopRotate(event, contact_i);
    });
}

function rotate(event, element) {
    const halfHeight = element.offsetHeight / 2;
    const halfWidth = element.offsetWidth / 2;
    element.style.transform = `rotateX(${-(event.offsetY - halfHeight) / 10}deg) rotateY(${(event.offsetX - halfWidth) / 10}deg)`;
}

function stopRotate(event, element) {
    element.style.transform = 'rotate(0)';
}

