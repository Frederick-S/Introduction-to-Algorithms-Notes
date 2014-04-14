// 1. Solution 1
test('Solution 1', function () {
    ok(solution1([4, -3, 5, -2, -1, 2, 6, -2]) == 11, 'The maximum subsequence sum of array [4, -3, 5, -2, -1, 2, 6, -2] is 11.');
    ok(solution1([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, 'The maximum subsequence sum of array [−2, 1, −3, 4, −1, 2, 1, −5, 4] is 6.');
    ok(solution1([-2, -3, 4, -1, -2, 1, 5, -3]) == 7, 'The maximum subsequence sum of array [-2, -3, 4, -1, -2, 1, 5, -3] is 7.');
});

// 2. Solution 2
test('Solution 2', function () {
    ok(solution2([4, -3, 5, -2, -1, 2, 6, -2]) == 11, 'The maximum subsequence sum of array [4, -3, 5, -2, -1, 2, 6, -2] is 11.');
    ok(solution2([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, 'The maximum subsequence sum of array [−2, 1, −3, 4, −1, 2, 1, −5, 4] is 6.');
    ok(solution2([-2, -3, 4, -1, -2, 1, 5, -3]) == 7, 'The maximum subsequence sum of array [-2, -3, 4, -1, -2, 1, 5, -3] is 7.');
});
