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

### 数组实例的属性
　　数组实例只有一个 `length` 属性，表示数组中元素的个数。

### 数组实例的方法
　　数组作为一种极为常用的数据结构，有很多的方法，下面介绍的都是定义在数组原型上的方法。

#### 插入/删除类操作

　　插入/删除类操作将会改变原数组。

**Array.prototype.push(element1, ..., elementN)** *向数组末尾添加一个或者多个元素，返回数组新的长度*

```javascript
const arr = [1,2,3];
const arr2 = [7,8,9];
const len = arr.push(4, 5, 6, arr2);
console.log(arr);
console.log(len);

// [ 1, 2, 3, 4, 5, 6, [ 7, 8, 9 ] ]
// 7
```
从上面我们可以看到，`arr2` 是作为一个整体被添加到 `arr` 的末尾，有时候我们希望 `arr2` 合并到 `arr` 中，那么如何使用 `push` 方法实现数组的合并呢？答案是使用函数原型上的 `apply` 方法。

```javascript
const arr = [1,2,3];
const arr2 = [7,8,9];
arr.push.apply(arr,arr2);
console.log(arr);

// [ 1, 2, 3, 7, 8, 9 ]
```
`apply` 法将 `arr2` 中的每一个元素作为参数参数传递给 `push` 方法，相当于 `arr.push(4,5,6)`, 关于 `apply` 的更多解释请参考 [Function.prototype.apply()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)

但是上面的实现是有缺陷的，它不能同时传入单个值的参数和数组参数，因为 `apply` 方法只接收一个数组参数，解决这一问题的方式是使用扩展运算符。ECMAScript6 定义了由三个点(...)组成的扩展运算符，它将数组转为用逗号分隔的参数序列。我们可以也使用它来实现数组的合并
```javascript
const arr = [1,2,3];
const arr2 = [7,8,9];
arr.push(4,5,6, ...arr2);
console.log(arr);

// [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
这样就简单多了。

**Array.prototype.pop()** *删除数组的最后一个元素，返回该元素的值，当数组为空时返回undefined*

```javascript
const arr = ['a','b']
console.log(arr.pop());  // b
console.log(arr.pop());  // a
console.log(arr.pop());  // undefined
```

**Array.prototype.unshift(element1, ..., elementN)** *向数组开头添加一个或者多个元素，返回数组新的长度*

```javascript
const arr = [1,2,3];
const arr2 = [7,8,9];
const len = arr.unshift(4, 5, 6, arr2);
console.log(arr);
console.log(len);

// [ 4, 5, 6, [ 7, 8, 9 ], 1, 2, 3 ]
// 7
```
传入多个参数时，插入数组中的顺序与作为参数时的顺序是一致的，同样你也可以使用上文提到的方法将一个数组合并到另一个数组的开头，这里就不再举例子了。

**Array.prototype.shift()** *删除数组的第一个元素，返回该元素的值，当数组为空时返回undefined*

```javascript
const arr = ['a','b']
console.log(arr.shift());  // b
console.log(arr.shift());  // a
console.log(arr.shift());  // undefined
```

**Array.prototype.reverse()** *反序数组中的元素的位置，返回反序后的数组*

```javascript
const arr = [1,2,3]
arr.reverse()
console.log(arr);  // [ 3, 2, 1 ]
```
配合 `apply` 或者 `call`, 该方法还可用于对类数组的反序，例如函数的 `arguments` 对象。

```javascript
function test() {
  Array.prototype.reverse.call(arguments);
  console.log(arguments)
}
test(1,2,3);

// [Arguments] { '0': 3, '1': 2, '2': 1 }
```

**Array.prototype.splice(start[, deleteCount[, item1[, item2[, ...]]]])** *删除/替换/增加元素，以数组的形式返回被删除的内容，若没有元素被删除则返回空数组*

　　该函数兼具删除、替换、增加三种功能，参数 `start`​ 指定修改的开始位置（从0计数）。如果超出了数组的长度，则从数组末尾开始添加内容；如果是负值，则表示从数组末位开始的第几位（从-1计数）；如果负数的绝对值大于数组的长度，则表示开始位置为第0位。
　　参数 `deleteCount` 表示要移除的数组元素的个数。如果 `deleteCount` 大于 `start` 之后元素的总数，则从 `start` 后面的元素都将被删除（含第 start 位）。如果 deleteCount 是 0 或者负数，则不移除元素。
　　`deleteCount` 之后的参数为将要被添加进数组的元素。

```javascript
const arr = [1,2,3]

// 只添加元素
arr.splice(1, 0, 4, 5, 6)
console.log(arr);  // [ 1, 4, 5, 6, 2, 3 ]

// 删除元素并添加元素，相当于替换
const result = arr.splice(1, 2, 7, 8, 9)
console.log(arr);  // [ 1, 7, 8, 9, 6, 2, 3 ]
console.log(result); // [ 4, 5 ]

// 只删除元素
arr.splice(1, 4)
console.log(arr);  // [ 1, 2, 3 ]

// 从倒数第二个位置删除元素，并添加新元素
arr.splice(-2, 1, 4, 5, 6)
console.log(arr);  // [ 1, 4, 5, 6, 3 ]
```


**Array.prototype.fill(value[, start[, end]])** *使用一个固定值填充数组，返回修改后的数组* **ES6新增**

　　参数 `value` 表示用来填充数组元素的值，`start` （可选） 表示起始索引，默认值为0, `end` （可选） 表示终止索引，默认值为数组长度。start,end 为一个左闭右开的区间。当 `start` 或 `end` 为负数时，则表示从数组末位开始的第几位（从-1计数）。

```javascript
const arr = [1,2,3,4,5];

arr.fill(0, 2, 4);
console.log(arr);  // [ 1, 2, 0, 0, 5 ]

arr.fill(0, -4, -3);
console.log(arr);  // [ 1, 0, 0, 0, 5 ]
```

**Array.prototype.copyWithin(target[, start[, end]])** *复制数组的一部分到同一数组中的另一个位置，不会改变原数组的长度，返回改变后的数组*

　　参数 `target` 表示复制的目标位置，如果是负数，将从末尾开始计算。如果其值超过数组的长度，将不会发生拷贝。`start` （可选） 表示被复制元素的起始位置， 默认值为0，如果是负数，`start` 将从末尾开始计算。`end` （可选） 表示被复制元素的结束位置，如果是负数，`end` 将从末尾开始计算。start,end 为一个左开右闭区间。若区间内的元素被复制到目标位置后超过数组的长度，则超过的部分将被舍弃。
```javascript
console.log([1,2,3,4,5].copyWithin(0, 2, 4));
console.log([1,2,3,4,5].copyWithin(3, 1, 4)); 

// [ 3, 4, 3, 4, 5 ]
// [ 1, 2, 3, 2, 3 ]
```

