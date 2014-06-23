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

// 2. Solution 2
function solution2(numbers) {
    var length = numbers.length, max = 0, sum = 0;
    for (var i = 0; i < length; i++) {
        sum = 0;
        for (var j = i; j < length; j++) {
            sum += numbers[j];

            if (sum > max) {
                max = sum;
            }
        }
    }

    return max;
}

// 3. Solution 3
function solution3(numbers, left, right) {
    var maxLeftSum = 0, maxRightSum = 0;
    var maxLeftBorderSum = 0, maxRightBorderSum = 0;
    var leftBorderSum = 0, rightBorderSum = 0;
    var center = 0, i = 0, j = 0;

    if (left === right) {
        return numbers[left] > 0 ? numbers[left] : 0;
    }

    center = parseInt((left + right) / 2);
    maxLeftSum = solution3(numbers, left, center);
    maxRightSum = solution3(numbers, center + 1, right);

    for (i = center; i >= left; i--) {
        leftBorderSum += numbers[i];
        if (leftBorderSum > maxLeftBorderSum) {
            maxLeftBorderSum = leftBorderSum;
        }
    }

    for (j = center + 1; j <= right; j++) {
        rightBorderSum += numbers[j];
        if (rightBorderSum > maxRightBorderSum) {
            maxRightBorderSum = rightBorderSum;
        }
    }

    return Math.max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum);
}

// 4. Solution 4
function solution4(numbers) {
    var thisSum = 0, maxSum = 0;

    for (var i = 0, length = numbers.length; i < length; i++) {
        thisSum += numbers[i];

        if (thisSum > maxSum) {
            maxSum = thisSum;
        } else if (thisSum < 0) {
            thisSum = 0;
        }
    }

    return maxSum;
}
