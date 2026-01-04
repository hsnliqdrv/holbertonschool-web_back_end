export default class Building {
    constructor(sqft) {
        if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
            throw new Error("Class extending Building must override evacuationWarningMessage");
        }
        if (typeof sqft !== 'number') {
            throw new Error('Sqft must be a number');
        }
        this._sqft = sqft;
    }

    get sqft() {
        return this._sqft;
    }

    evacuationWarningMessage() { }
}