function replace(s) {
    return s.split('q').join('e');
}

var input = 'querty';
console.log(replace(input));

input = 'hqllo my namq is hyqwon';
console.log(replace(input));