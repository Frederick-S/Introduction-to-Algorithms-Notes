function setLeftHalfToN(b, n) {
    return (b & (255 >> 4)) | (n << 4);
}

function setRightHalfToN(b, n) {
    return (b & (255 << 4)) | n;
}

function getLeftHalf(b) {
    return (b & (255 << 4)) >> 4;
}

function getRightHalf(b) {
    return b & (255 >> 4);
}

function solution1() {
    var b = 0;
    for (b = setLeftHalfToN(b, 1); getLeftHalf(b) <= 9; b = setLeftHalfToN(b, getLeftHalf(b) + 1)) {
        for (b = setRightHalfToN(b, 1); getRightHalf(b) <= 9; b = setRightHalfToN(b, getRightHalf(b) + 1)) {
            if (getLeftHalf(b) % 3 !== getRightHalf(b) % 3) {
                console.log("A = " + getLeftHalf(b) + ", B = " + getRightHalf(b));
            }
        }
    }
}
