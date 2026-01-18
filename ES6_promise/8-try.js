export default function divideFunction(numberA, numberB) {
    if (numberB === 0) {
        throw new Error('cannot divide by 0');
    }
    return numberA / numberB;
}