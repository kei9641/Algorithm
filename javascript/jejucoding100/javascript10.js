var n = 5;

for (var i=1; i<=5; i+=1) {
    var line = '';
    for (var j=5-i; j>0; j-=1) {
        line += ' ';
    }
    for (var k=1; k<=i*2-1; k+=1) {
        line += '*'
    }
    console.log(line);
}
