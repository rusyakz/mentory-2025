'use strict'


let name = prompt('What is your name?');

// if (typeof name === 'string') {
//     alert(`Hello ${name}`);
// } else {
//     alert('Hello World!');
// }

function hello() {
    if (name) {
        userName.innerHTML = `Hello ${name}`;
    } else {userName.innerHTML = 'Hello';}
}


let userName = document.getElementById('hello-user');

document.addEventListener('DOMContentLoaded', hello)

console.log(name);