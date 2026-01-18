export default function guardrail(mathFunction) {
    const queue = [];
    let error = null;

    try {
        const result = mathFunction();
        queue.push(result);
    } catch (err) {
        error = err.toString();
        queue.push(error);
    } finally {
        queue.push('Guardrail was processed');
    }

    return queue;
}