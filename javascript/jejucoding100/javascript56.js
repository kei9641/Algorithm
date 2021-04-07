var nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England' : 242900,
};

var gap = nationWidth['korea'];
var nation = '';
for (var [key, value] of Object.entries(nationWidth)) {
    if (key !== 'korea') {
        if (gap > Math.abs(nationWidth['korea'] - value)) {
            gap = Math.abs(nationWidth['korea'] - value);
            nation = key;
        }
    }
}

console.log(nation, gap);