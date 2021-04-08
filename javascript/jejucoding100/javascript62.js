var str = 'aacdddddddddfffffffffgghhh';
var word = {
    'a': Number(null),
    'b': Number(null),
    'c': Number(null),
    'd': Number(null),
    'e': Number(null),
    'f': Number(null),
    'g': Number(null),
    'h': Number(null)
};
var result = '';

for (var s of str) {
    word[s]++;
}

for (var value of Object.values(word)) {
    result += value;
}
console.log(result);
