var input = '원범 원범 혜원 혜원 혜원 혜원 유진 유진'.split(' ');
var candidates = {};
var elect = '';
var vote = 0;

for (var i=0; i<input.length; i++) {
    var person = input[i];

    if (candidates[person]) {
        candidates[person] += 1;
    } else {
        candidates[person] = 1;
    }
    
    if (vote < candidates[person]) {
        elect = person;
        vote = candidates[person];
    }
}

console.log(`${elect}(이)가 총 ${vote}표로 반장이 되었습니다.`);
console.log(Object.keys(candidates))