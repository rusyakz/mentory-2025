'use strict'




// #1 Обмен значениями двух переменных
let a = 22, b = 33;

[a, b] = [b, a];



//#2 Проверка чётного или нечётного числа
function isEven(num) {
    return num % 2 === 0
}

// #3 Сумма чисел от 1 до N

// цикл for
function sumTo(num) {
    let result = 0;
    for (let i = 1; i <= num; i++) {
        result += i
    }
    return result
}

// рекурсия
function sumTo2(num) {
    if (num === 1) {
        return num
    }
    return num + sumTo2(num-1)
}


// #4 Переворот строки
function reverseString(str) {
    return str.split('').reverse().join('')
}

// #5 Фильтрация массива по чётным числам
function filterEven(arr) {
    let result = [];

    for (let i = 0; arr.length > i; i++) {
        if (arr[i] % 2 === 0) {
            result.push(arr[i])
        }
    }
    return result
}

// #6 Конвертер температуры
function celsiusToFahrenheit(c) {
    return c * 9/5 + 32
}

function fahrenheitToCelsius(f){
    return (f - 32) * 5/9
}


// #7 Проверка строки на палиндром
function isPalindrome(str) {
    str = str.split(' ').join('').toLowerCase()
    let strMirros = str.split('').reverse().join('')
    return str === strMirros
}

function isPalindrome2(str) {
    str = str.split(' ').join('')
    if (str.length <= 1) {
        return true
    }
    if (str.at(0) === str.at(-1)) {
        return isPalindrome(str.slice(1, -1))
    }
    return false
}

// #8 Сумма всех элементов массива (for)
function sumArray(arr) {
    let result = 0;
    for (let i = 0; i < arr.length; i++) {
        result += arr[i]
    }
    return result;
}

// #9 Найти самое длинное слово в массиве строк (for…of)
function longestWord(words) {
    let temp = 0;
    let result;
    for (let word of words) {
        if (word.length > temp) {
            temp = word.length;
            result = word
        }
    }
    return result;
}


function longestWord2(words) {
    let result = words[0]
    for (let word of words) {
        if (word.length > result.length) {
            result = word
        }
    }
    return result
}


// #10 Подсчитать количество свойств в объекте (for…in)
function countProps(obj) {
    let result = 0;
    for (let key in obj) {
        ++result
    }
    return result
}



// #11 Вывести числа от 1 до N (while)
function printTo(n) {
    let temp = 1;
    while (n >= temp) {
        console.log(temp++)
    }
}


// #12 Найти число в массиве вручную (без includes)
function  manualFindIndex(arr, value) {
    for (let i = 1; i <= arr.length; i++) {
        if (arr[i] === value) {
            return i
        }
    }
}
