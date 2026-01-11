function cleanSet(set, startString) {
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