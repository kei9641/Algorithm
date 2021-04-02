var input = '20 30 40';
var grade = input.split(' ');
var sum = 0;

for (var i=0; i<grade.length; i+=1) {
    sum += parseInt(grade[i], 10);
}

var average = Math.floor(sum / 3);
console.log(average);