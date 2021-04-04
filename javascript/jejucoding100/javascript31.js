var arr = [];

// 인덱스 조회 => O(1)
arr[1];

// 마지막에 추가 => O(1)
arr.push(5);

// 복제 => O(n)
arr.slice();

// 마지막 삭제 => O(1)
arr.pop();

// 값 조회 => 최대 O(n)
arr.includes(5);