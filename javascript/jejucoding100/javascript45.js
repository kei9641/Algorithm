var day = new Date();
var second = day.getTime();
var year = parseInt(second / (3600 * 24 * 365 * 1000), 10) + 1970;

console.log(year);