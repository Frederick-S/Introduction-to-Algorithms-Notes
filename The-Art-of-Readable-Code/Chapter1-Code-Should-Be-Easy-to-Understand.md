# Chapter 1: Code should be easy to understand
## Key ideas
1. Code should be easy to understand.
2. Code should be written to minimize the time it would take for someone else to understand it.

## Smaller is not always better
一般来说，精简的代码很可能会比冗长的代码更容易理解。比如下面这组例子：
```js
for (var node = list.head; node != null; node = node.next) {
    print(node.data);
}
```
和
```js
var node = list.node;
if (node == null) {
    return;
}

while (node.next != null) {
    print(node.data);
    node = node.next;
}

if (node != null) {
    print(node.data);
}
```
虽然上面两段代码完成的是相同的事情，但是显然第一段代码更清晰易懂。不过，有时候简短的代码反而会降低可读性。比如：
```js
assert((!(bucket = findBucket(key))) || !bucket.isOccupied());
```
虽然这段代码很短，但是并不能让人快速理解，一个较清晰易懂的替代方案是：
```js
bucket = findBucket(key);
if (bucket != null) {
    assert(!bucket.isOccupied());
}
```
另外，有效的注释也能增强代码的可读性，虽然这会增加代码的行数。例如：
```js
// Fast version of "hash = (65599 * hash) + c"
hash = (hash << 6) + (hash << 16) - hash + c;
```
