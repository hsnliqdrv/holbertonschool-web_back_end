export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const value = array[idx];
    array[idx] = value + appendString;
  }

  return array;
}