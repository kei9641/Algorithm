function quickSort(arr){
    if (arr.length <= 1){
        return arr;
    }

    const pivot = arr[0];
    const left = [];
    const right = [];

    for (let i=1; i<arr.length; i++){
        if(pivot > arr[i]){
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }
    return quickSort(left).concat(pivot, quickSort(right));
}

const array = '4 2 3 8 5'.split(' ').map(n => parseInt(n, 10));

console.log(quickSort(array));