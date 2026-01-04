import Currency from "./3-currency";

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new Error('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw new Error('Currency must be an object');
    }
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(price, conversionRate) {
    if (!(price instanceof Pricing)) {
      throw new Error('Price must be an instance of Pricing');
    }
    if (typeof conversionRate !== 'number') {
      throw new Error('Conversion rate must be a number');
    }
    const newAmount = price.amount * conversionRate;
    return new Pricing(newAmount, price.currency);
  }
}