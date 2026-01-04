export default class Car {
    constructor(brand, motor, color) {
        if (typeof brand !== 'string') {
            throw new Error('Brand must be a string');
        }
        if (typeof motor !== 'string') {
            throw new Error('Motor must be a string');
        }
        if (typeof color !== 'string') {
            throw new Error('Color must be a string');
        }
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

    get brand() {
        return this._brand;
    }

    get motor() {
        return this._motor;
    }

    get color() {
        return this._color;
    }

    cloneCar() {
        return new Car(this._brand, this._motor, this._color);
    }
}