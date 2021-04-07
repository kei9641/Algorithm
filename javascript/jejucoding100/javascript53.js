var bracket = {
    '(': ')',
    '[': ']',
    '{': '}'
};

function validate(s) {
    var stack = [];
    for (var i = 0; i < s.length; i++) {
        if (bracket.hasOwnProperty(s[i])) {
            stack.push(s[i]);
        } else if (stack.length) {
            var lastStack = stack.pop();
            if (bracket[lastStack] !== s[i]) {
                return 'NO';
            }
        } else {
            return 'NO';
        }
    }

    if (stack.length) {
        return 'NO';
    }
    return 'YES';
}

var input = '(())'.split('');
console.log(validate(input));

input = '()())'.split('');
console.log(validate(input));

input = '{()())'.split('');
console.log(validate(input));