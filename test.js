// 'use strict'
//
//
// class Auto {
//     #odometer;
//
//     constructor(manufacturer, model, year, odometer) {
//         this.manufacturer = manufacturer;
//         this.model = model;
//         this.year = year;
//         this.#odometer = odometer
//     }
//
//     getOdometer() {
//         return this.#odometer;
//     }
//
//     editOdometer(value) {
//         if (typeof value === 'number' && value > this.#odometer)  {
//             this.#odometer = value;
//         } else {
//             return 'Проверте введенные значения';
//         }
//     }
//
//     updateOdometer(value) {
//         if (typeof value === 'number')  {
//             this.#odometer += value;
//         } else {
//             return 'Не верное значение';
//         }
//     }
// }
//
// class GasCar extends Auto {
//     constructor(manufacturer, model, year, odometer, enginValue) {
//         super(manufacturer, model, year, odometer);
//
//         this.enginValue = enginValue;
//     }
// }
//
//
// class ElectroCar extends Auto {
//     constructor(manufacturer, model, year, odometer, enginPower) {
//         super(manufacturer, model, year, odometer);
//
//         this.enginPower  = enginPower;
//     }
// }
//
//
//
// let tesla = new ElectroCar('tesla', 'model y', 2022, 10, 1);
//
// console.log(tesla.getOdometer());
//
// tesla.updateOdometer(22);
//
// console.log(tesla.getOdometer());
//
// console.log(typeof(typeof(10)));
//
//
//
//
// class Triangle {
//     constructor(a, b, c) {
//         this.a = a;
//         this.b = b;
//         this.c = c;
//     }
// }




const a = Math.random()

console.log(a)



