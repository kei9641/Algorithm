function gugudan(n) {
    var multiple = [];
    for (var i=1; i<10; i++) {
        multiple.push(n*i); 
    }
    return multiple.join(' ');    
}

var input = parseInt('2', 10);
console.log(gugudan(input));