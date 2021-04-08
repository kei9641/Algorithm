var n = 24;
var carry = 0;

while (1) {
    if (n % 7 == 0) {
        carry += parseInt(n / 7, 10);
        break;
    }
    n -= 3;
    carry += 1;
    if (n < 0) {
        carry = -1;
        break;
    }
}
console.log(carry);