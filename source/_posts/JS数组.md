---
title: JS数组
reward: true
date: 2019-12-30 10:43:51
permalink: 13
categories: [前端, JavaScript]
tags:
---

　　数组是 JavaScript 中最为常用的数据类型之一，一个数组中可以存储多个相同类型或不同类型的元素，元素的类型可以是基本类型也可以是数组类型，本文就JS数组的属性与方法做一个简单的介绍，争取用丰富的例子让读者明晰数组中常用函数的用法，同时尝试实现一些数组的方法。

### 数组的构造

- **直接构造**
　　最常用也最明显的方式就是直接写一个用中括号括起来的数组，如 `const arr = [1,2,3];`
- **构造函数**
　　使用 `Array` 构造函数构造一个数组，函数原型为 `new Array(element0, element1[, ...[, elementN]])`，如 `const arr = new Array(1,2,3);` **需要注意的是，当只向函数传递一个数值参数时，并不会构造出一个只包含一个元素的数组，该参数将作为数组的长度构造出一个含有N个空元素的数组**，如 `const arr = new Array(5)` 则 arr 的值为 `[ <5 empty items> ]`
- **Array.from**
　　`Array.from` 方法用于从一个类数组对象或者可迭代对象生成数组，函数原型为 `Array.from(arrayLike[, mapFn[, thisArg]]);` 函数生成的数组将是一个全新的数组，改变该数组不会影响原来的数组，例如 
```javascript
const arr = [1,2,3]; 
const arrCopy1 = arr;
const arrCopy2 = Array.from(arr);
arrCopy1[0] = 8;
arrCopy2[1] = 10;
console.log(arr)  // [8,2,3]
console.log(arrCopy1)  // [8,2,3]
console.log(arrCopy2)  // [1,10,3]
```
　　从类数组生成，那么什么是类数组呢？按照MDN的解释，类数组是具有length属性和索引元素的对象，因为是类数组，所以它不具备一般意义上的数组所拥有的方法，如 `const arrLike = {'0':'a', '1':'b', '2':'c', length:3};` arrlike 具有 length 属性且其元素是可被索引的。
```javascript
const arrLike = {'0':'a', '1':'b', '2':'c', length:3};
const arrCopy = Array.from(arrLike);
console.log(arrCopy)  // ['a','b','c']
```
　　`Array.from` 默认从索引0开始查找元素，且生成的数组长度与类数组的 `length` 属性值一致，当找不到该索引时会将该索引对应的值设置为 `undefined`.
```javascript
const arrLike = {'1':'a', '2':'b', '3':'c', length:3};
const arrCopy = Array.from(arrLike);
console.log(arrCopy)  // [ undefined, 'a', 'b' ]

// 从0开始查找，找不到设置为 undefined, 继续查找，找到索引为1和索引为2的元素，
// 因为length属性的值为3, 则停止查找
```
　　函数的 `arguments` 对象是一种常见的类数组，我们可以使用 `Array.from` 函数将其转换为数组。
```javascript
function test() {
  console.log(arguments);
  console.log(Array.from(arguments));
}

test(1,2,3)

// [Arguments] { '0': 1, '1': 2, '2': 3 }
// [ 1, 2, 3 ]
```
　　那么什么又是可迭代对象呢？**可迭代对象内部通常都有一个迭代器，可以通过对迭代器的调用顺序的访问对象内的每一个元素**。数组属于可迭代对象，ES6中的 `Set` 和 `Map` 也属于可迭代对象，关于可迭代对象的更多内容请参考网友写的一片文章[【ES6】迭代器与可迭代对象](https://segmentfault.com/a/1190000016824284)
例如，ES6中的[生成器函数](http://es6.ruanyifeng.com/#docs/generator)返回一个可迭代对象，我们可以将该可迭代对象转换为数组
```javascript
function* test() {
  yield 1 + 2;
  yield 3 + 4;
  yield 5 + 7;
}

const gen = test();
console.log(gen)  // Object [Generator] {}
console.log(Array.from(gen)) // [3,7,12]
```
- **Array.of**
　　上文说道当我们只向 `Array` 构造函数传递一个数值时，不会创建包含单一元素的数组，而会创建包含N个元素的空数组。而 `Array.of` 就是解决这一问题的，向 `Array.of` 传递一个数值时将会创建出包含单一元素的数组。除此之外与构造函数无任何不同。
```javascript
const arr = Array.of(1);
console.log(arr);  // [1]
```

### 数组的属性
　　数组只有一个 `length` 属性，表示数组中