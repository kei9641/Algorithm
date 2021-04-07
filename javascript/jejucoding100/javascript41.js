var num = 5;

function isPrime(n) {
    if (n == 1) {
        return 'NO';
    }

    for (var i=2; i<n; i++) {
        if (n % i == 0) {
            return 'NO';
        }
    }
    return 'YES';
}

console.log(isPrime(num));