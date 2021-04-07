function one(n) {
    function two(m) {
        return m ** n;
    }
    return two;
}

var a = one(2);
var b = one(3);
var c = one(4);

console.log(a(10));
console.log(b(10));
console.log(c(10));