export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new Error('Length must be a number');
    }
    if (!(students instanceof Array)) {
      throw new Error('Students must be an array');
    }
    if (!students.every(student => typeof student === 'string')) {
      throw new Error('All students must be strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }
  
  get name() {
    return this._name;
  }
    get length() {
    return this._length;
  }
    get students() {
    return this._students;
  }
}