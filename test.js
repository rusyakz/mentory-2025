'use strict'

// let bb = 'rustem man'
//
// let test = {
//     bb: 'tt'
// }
//
// console.log(test['bb']);




let test = (2 > 3) ? true : 22;

console.log(test)


let a = 22;

for (let i = 0; i < a; i++) {
    console.log(i)
}





let arr = [1, 2, 0, 3];
let arr2 = [4, 5, 6];

arr = arr.concat(arr2); //канкатинаяция массивов
let m = arr.pop(); // удаляет последний элемент, можно удаляемый объект в отделюную переменную записать
arr.push(7); // Добавить в конец массива один объект
arr.unshift(-1, 0); // Добавить в начале массива объекты перечисленные через запятую
arr.shift(); // Удалить первый объект
arr = arr.slice(1, -2); // Срез массива, указав начальный и последний индек объекта
arr.sort(); // сортируют массив
arr.reverse(); // сортирует в обратном порядке
// arr = arr.toString() // Склеевает объекты  массива в строку через запятую без пробела
// arr = arr.toLocaleString() //
arr.fill(4, 2, 4) // Заполняет массив данными value в диапазоне индексов start и end
let secondObj = arr.at(2) // обращаться по индкусу объекта в массиве
let arrLength = arr.length; // это конечно не метод массива, но можно получить количество объектов массива


console.log(arr)
console.log(m);
console.log(secondObj)
console.log(arrLength);