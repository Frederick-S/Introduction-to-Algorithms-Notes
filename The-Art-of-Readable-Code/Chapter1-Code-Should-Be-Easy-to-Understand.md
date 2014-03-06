# Chapter 1: Code should be easy to understand
## Key Idea 1: Code should be easy to understand
这是贯穿全书的一个核心，书中剩下的部分都是围绕这个核心展开的，也就是如何使得代码易于理解。 
## Key Idea 2: Code should be written to minimize the time it would take for someone else to understand it
什么样的代码是可读性强的？一个最基本的原则就是尽可能的减少理解代码所需要的时间。
## Smaller is not always better
一般来说，精简的代码很可能会比冗长的代码更容易理解。比如下面这组例子：
```js
for (var node = list.head; node != null; node = node.next) {
    print(node.data);
}
```
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
```js
bucket = findBucket(key);
if (bucket != null) {
    assert(!bucket.isOccupied());
}
```
虽然第一段代码更短，但是第二段代码更容易让人快速理解。
