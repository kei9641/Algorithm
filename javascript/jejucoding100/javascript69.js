function primeList(num) {
    var sieve = [false, false];
    for (var n = 2; n < num; n++) {
        sieve.push(true);
    }

    for (var i = 2; i < parseInt(num ** 0.5, 10) + 1; i++) {
        if (sieve[i]) {
            for (var j = i + i; j < num; j += i) {
                sieve[j] = false;
            }
        }
    }
    for (var k = 2; k < num; k++) {
        if (sieve[k]) {
            prime.push(k);
        }
    }
}

var num = 100;
var prime = [];
primeList(num);

var left = 0;
var right = prime.length - 1;
var sum = prime[left] + prime[right];
var goldbach = [];

while (left < right) {
    if (sum < num) {
        left += 1;
    } else if (sum > num) {
        right -= 1;
    } else {
        goldbach.push([prime[left], prime[right]]);
        left += 1;
        right -= 1;
    }
    sum = prime[left] + prime[right];
}
console.log(goldbach);