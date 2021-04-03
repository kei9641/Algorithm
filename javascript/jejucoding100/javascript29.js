function isUpper(s) {
    if (s == s.toUpperCase()) {
        return 'YES';
    } else {
        return 'NO';
    }
}

var input = 'A';
console.log(isUpper(input));

input = 'a';
console.log(isUpper(input));