function accessRide(height) {
    if (height >= 150) {
        return 'YES';
    } else {
        return 'NO';
    }
}

var height = 160;
console.log(accessRide(height));

height = 120;
console.log(accessRide(height));