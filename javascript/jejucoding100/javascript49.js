var nums = '10 9 8 7 6 5 4 3 2 1'.split(' ').map((n) => {
    return parseInt(n, 10);
})

var maxNum = nums.reduce((a, b) => {
    return a > b ? a : b;
})
console.log(maxNum);