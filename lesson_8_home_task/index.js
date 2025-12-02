'use strict'


const form = document.getElementById('form');


function eventListeners(event) {
    console.log(`Поле "${event.target.name}" изменено:`, event.target.value);
}

form.addEventListener('input', eventListeners);



function submit(event) {
    event.preventDefault(); // чтобы не перезагружалась страница

    const formData = new FormData(form);
    const obj = {};

    formData.forEach((value, key) => {
        obj[key] = value;
      });
      console.log("Все данные формы:", obj);
}


form.addEventListener('submit', submit);