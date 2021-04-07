var n = 1000;
var one = 0;

for (var i = 0; i < n; i++) {
    var num = i;
    while (num) {
        if (num % 10 === 1) {
            one += 1;
        } 
        num = parseInt(num / 10, 10);
    }
}

console.log(one);