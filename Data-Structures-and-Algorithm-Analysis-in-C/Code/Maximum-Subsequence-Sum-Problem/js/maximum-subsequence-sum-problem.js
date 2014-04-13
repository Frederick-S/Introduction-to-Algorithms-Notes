// 1. Solution 1
function solution1(numbers) {
    var length = numbers.length, max = 0, sum = 0;
    for (var i = 0; i < length; i++) {
        for (var j = i; j < length; j++) {
            sum = 0;
            for (var k = i; k <= j; k++) {
                sum += numbers[k];
            }

            if (sum > max) {
                max = sum;
            }
        }
    }

    return max;
}
