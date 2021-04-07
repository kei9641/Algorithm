var profit = '123456789';

for (var i = 3; i < profit.length; i += 4) {
    profit = profit.slice(0, -i).concat(',', profit.slice(-i));
}

console.log(profit)