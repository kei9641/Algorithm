var input = 'aaabbbbcdddd';
var word = {};
var zipStr = '';

for (var s of input) {
    if (word[s]) {
        word[s] += 1;
    } else {
        word[s] = 1;
    }
}

for (var [key, value] of Object.entries(word)) {
    zipStr += key + value;
}
console.log(zipStr)