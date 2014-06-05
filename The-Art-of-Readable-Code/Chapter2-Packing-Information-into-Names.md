# Chapter 2: Packing information into names
## Key ideas
1. Pack information into your names.
2. It’s better to be clear and precise than to be cute.

## Choose specific words
正如用外语和别人交谈一样，即使发音不太标准，但只要用词准确，听的人也一样能听明白。而如果用词不当，哪怕发音再标准，听的人也可能会一头雾水。所以选择明确的用词对于命名是很重要的，反之，则可能会让阅读代码的人产生困惑，例如：
```js
function getPage(url) {
    // ...
}
```
在上面的例子中，`get` 是一个非常宽泛的词，`getPage` 并不能明确的表达这个方法的用途，它有可能是从缓存或数据库中获取页面，也有可能从网络中抓取页面。如果是从网络中抓取页面，那么 `fetchPage` 或者 `downloadPage` 可能更好。

## Avoid generic names like tmp and retval
类似 `tmp`，`temp`，`retval` 是比较常见的命名，但是，一般情况下，这样的命名并没有包含足够的信息。如果这个变量只出现在几行代码里，那么我们可能并不难理解它的含义，但是如果它出现在了一段较长的代码里，在阅读代码的过程中，如果只凭 `tmp` 这样的命名，我们可能已经忘了它是做什么的。比如：
```js
// 虽然使用了 tmp 来命名，但是我们还是可以明白 tmp 表示当前用户
var tmp = Context.getCurrent().getCurrentUser();
if (tmp.isAdmin) {
    // Do something
} else {
    // Do something
}
```
```js
var tmp = Context.getCurrent().getCurrentUser();
if (tmp.isAdmin) {
    // Do something
} else {
    // Do something
}

...

// 100 行代码之后
// tmp 是什么？？？
var accountName = tmp.accountName;
```
又比如：
```js
var euclideanNorm = function (v) {
    var retval = 0.0;
    for (var i = 0, length = v.length; i < length; i++) {
        retval += v[i] * v[i];
    }

    return Math.sqrt(retval);
}
```
从字面上看，`retval` 表示返回值，但是并不能表达出这个变量在上面的方法中的意义。一个可能比较好的命名是 `sumSquares`。

**Advice: The name retval doesn’t pack much information. Instead, use a name that describes the variable’s value.**

不过，在某些情况下，类似于 `tmp` 的命名是适用的。
### tmp
```js
if (right < left) {
    tmp = right;
    right = left;
    left = tmp;
}
```
在这个例子里，`tmp` 就是一个临时变量，充当交换两个变量的值的媒介。

### Loop iterators
单独的 `i`，`j` 并没有什么实际意义，但是它们被广泛使用在循环中。
```js
for (var i = 0, length = numbers.length; i < length; i++) {
    sum += numbers[i];
}
```
不过，当嵌套的循环多了的时候，`i`，`j`，`k` 就可能让人混乱，容易写错。
```js
for (var i = 0; i < clubs.size(); i++) {
    for (var j = 0; j < clubs[i].members.size(); j++) {
        for (var k = 0; k < users.size(); k++) {
            if (clubs[i].members[j] == users[k]) {
                console.log("user[" + k + "] is in club[" + i + "]");
            }
        }
    }
}
```
所以，可以考虑用更清晰的命名来代替上面例子中的 `i`，`j`，`k`，比如 `ci`，`mj`，`uk`，这样就比较容易明白 `ci`，`mj`，`uk` 分别对应 `clubs`，`members`，`users`。  
```js
for (var ci = 0; ci < clubs.size(); ci++) {
    for (var mj = 0; mj < clubs[ci].members.size(); mj++) {
        for (var uk = 0; uk < users.size(); uk++) {
            if (clubs[ci].members[mj] == users[uk]) {
                console.log("user[" + uk + "] is in club[" + ci + "]");
            }
        }
    }
}
```
### a, b, c
与 `i`，`j` 类似，`a`，`b`，`c` 也没有实际意义，但是在一些情况下，它们也是适用的，比如：
```js
function compare(a, b) {
    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}

var numbers = [4, 2, 5, 1, 3];
numbers.sort(compare);
```

## Attaching extra information to a name
