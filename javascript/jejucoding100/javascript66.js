var tops = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG", "EFGHZ"];
var rule = "ABD";
var result = [];

function chekc(top) {
    var index = -1;
    for (var block of top) {
        if (rule.includes(block)) {
            if (rule.indexOf(block) < index) {
                return "불가능";
            } else {
                index = rule.indexOf(block);
            }
        }
    }
    return "가능";
}

for (var top of tops) {
    result.push(chekc(top));
}
console.log(result);