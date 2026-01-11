function cleanSet(set, startString) {
    if (!(set instanceof Set) || typeof startString !== 'string') {
        return '';
    }
    const result = [];
    for (const item of set) {
        if (!item || typeof item !== 'string') {
            continue;
        }
        if (item.startsWith(startString)) {
            result.push(item.slice(startString.length));
        }
    }
    return result.join('-');
}

export default cleanSet;