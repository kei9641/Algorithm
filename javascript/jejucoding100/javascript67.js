var handShake = 59;
var n = 1;
var count = 0;

while (1) {
    if (parseInt(n * (n - 1) / 2, 10) > handShake) {
        break;
    } 
    n += 1;
}

count = handShake - parseInt((n - 1) * (n - 2) / 2, 10);
console.log([count, n]);