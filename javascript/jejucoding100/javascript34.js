function isSort(row) {
    var height = 0;
    for (var i=0; i<row.length; i++) {
        var student = parseInt(row[i], 10);
        if (height > student) {
            return 'NO';
        } else {
            height = student;
        }
    }
    return 'YES';
}

var input = '176 156 155 165 166 169'.split(' ');
console.log(isSort(input));

input = '155 156 165 166 169 176'.split(' ');
console.log(isSort(input));