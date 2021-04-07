var limit = 50;
var n = 5;
var friends = [];
for (var i=0; i<n; i++) {
    friends.push(20);
}

var ride = 0;
var weight = 0;
while (ride < n) {
    weight += friends[ride];
    if (weight <= limit) {
        ride += 1;
    } else {
        break;
    }
}

console.log(ride);