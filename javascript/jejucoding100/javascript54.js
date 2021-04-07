function isSequence(input) {
    input.sort((a, b) => {
        return a - b;
    });

    var stamp = input[0];
    for (var i = 1; i < input.length; i++) {
        if (input[i] - 1 !== stamp) {
            return 'NO';
        }
        stamp = input[i];
    }
    return 'YES';
}

var input = '1 2 3 4 5'.split(' ').map((n) => {
    return parseInt(n, 10);
});
console.log(isSequence(input));

input = '1 4 2 6 3'.split(' ').map((n) => {
    return parseInt(n, 10);
});
console.log(isSequence(input));