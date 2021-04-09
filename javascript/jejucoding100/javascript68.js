var timeTable = ["12:30", "13:20", "14:13"];
var currentTime = "12:40";
var result = [];

for (var arriveTime of timeTable) {
    if (arriveTime < currentTime) {
        result.push('지나갔습니다.');
    } else {
        var hour = parseInt(arriveTime.slice(0, 2), 10) - parseInt(currentTime.slice(0, 2), 10);
        var minute = parseInt(arriveTime.slice(-2), 10) - parseInt(currentTime.slice(-2), 10);
        if (minute < 0) {
            hour -= 1;
            minute += 60;
        }
        result.push(hour.toString().padStart(2, '0').concat('시간 ', minute.toString().padStart(2, '0'), '분'));
    }
}

console.log(result);