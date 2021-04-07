var input = '97 86 75 66 55 97 85 97 97 95'.split(' ').map((n) => {
    return parseInt(n, 10);
});

input.sort((a, b) => {
    return b - a;
});

var candy = 0;
var rank = 0;
var grade = 0;
var i = 0;

while (rank < 3) {
    if (grade == input[i]) {
        candy += 1
    } else {
        grade = input[i];
        rank += 1
        candy += 1
    }

    i += 1
}

console.log(candy);