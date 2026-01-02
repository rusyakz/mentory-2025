
// Класс автомобиль
class Car {
    #odometer;
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.#odometer = 0;
    }

// Информация об автомобиле
    getCarInfo() {
        let carInfo = 'You car is ' + this.make;
        carInfo += ', model is ' + this.model + ', year ' + this.year;
        return carInfo;
    }

// Данные одометра
    showOdometer() {
        return this.#odometer;
    }

// Обновление данных одометра
    odometerUpdate(value) {
        if (this.#odometer > value) {
            console.log(`Odometer value can not be less than ${this.#odometer}`);
        } else {
            this.#odometer = value;
        }
    }

// Увеличение значения одометра
    odometerPlus(value) {
        if (value <= 0) {
            return 'Value can not be less than 0';
        } else {
            this.#odometer += value;
        }
    }
}

// Класс электромобиль, наследуется от класса Car
class ElectoCar extends Car {
    constructor(make, model, year, type) {
        super(make, model, year);
        this.type = type;
    }

    // Переназначение метода
    getCarInfo() {
        let carInfo = 'You car is ' + this.make;
        carInfo += ', model is ' + this.model + ', year ' + this.year;
        carInfo += ', Type is' + this.type;
        return carInfo;
    }
}
