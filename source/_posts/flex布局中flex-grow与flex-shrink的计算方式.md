---
title: flex布局中flex-grow与flex-shrink的计算方式
date: 2019-12-08 21:57:10
tags:
---

　　CSS 中的 Flex(弹性布局) 可以很灵活的控制网页的布局，其中决定 Flex 布局内项目宽度/高度的是三个属性：
flex-basis, flex-grow, flex-shrink. 

　　flex-basis 决定了项目占据的主轴空间，你可以为其指定一个具体的像素值，也可以指定其占据父元素的百分比


```html
  <style>
    .parent {
      width: 500px;
      display: flex;
      margin-bottom: 15px;
      text-align: center;
      background-color: #eeeeee;
    }

    /** 像素值*/
    .parent:nth-child(1) .child1 {
      flex-basis: 100px;
      background-color: #356969
    }
    .parent:nth-child(1) .child2 {
      flex-basis: 200px;
      background-color: #369925;
    }

    /** 百分比 */
    .parent:nth-child(2) .child1 {
      flex-basis: 10%;
      background-color: #356969
    }
    .parent:nth-child(2) .child2 {
      flex-basis: 20%;
      background-color: #369925;
    }

    /** 自动 */
    .parent:nth-child(3) .child1 {
      flex-basis: 30%;
      background-color: #356969
    }
    .parent:nth-child(3) .child2 {
      flex-basis: auto;
      background-color: #369925;
    }
  </style>
  <div class="parent">
    <div class="child1">100px</div>
    <div class="child2">200px</div>
  </div>
  <div class="parent">
    <div class="child1">10%</div>
    <div class="child2">20%</div>
  </div>
  <div class="parent">
    <div class="child1">30%</div>
    <div class="child2">auto</div>
  </div>
```

![flex-basis](/assets/images/map/4/ar4-1.png)

