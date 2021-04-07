var month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
};

var week = ['WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE'];

var a = 5;
var b = 24;

var day = b - 1;
for (var i=1; i<a; i++) {
    day += month[i];
}

console.log(week[day % 7]);
