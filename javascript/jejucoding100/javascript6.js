var a = NaN;
if (a) {
    console.log('NaN은 True');
} else {
    console.log('NaN은 False');
}

a = 1;
if (a) {
    console.log('1은 True');
} else {
    console.log('1은 False');
}

a = "";
if (a) {
    console.log('""은 True');
} else {
    console.log('""은 False');
}

a = 0;
if (a) {
    console.log('0은 True');
} else {
    console.log('0은 False');
}

a = undefined;
if (a) {
    console.log('undefined은 True');
} else {
    console.log('undefined은 False');
}

// False 값 : null, undefined, 0, "", NaN, false