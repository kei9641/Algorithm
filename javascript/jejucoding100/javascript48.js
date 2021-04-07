var input = 'AAABBBcccddd'.split('');

for (var i in input) {
    if (input[i] == input[i].toUpperCase()) {
        input[i] = input[i].toLowerCase();
    } else {
        input[i] = input[i].toUpperCase();
    }
}
console.log(input.join(''));