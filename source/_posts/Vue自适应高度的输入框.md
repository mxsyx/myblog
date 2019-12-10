---
title: Vue自适应高度的输入框
reward: true
date: 2019-12-10 22:15:19
permalink: 10
categories: VueJS
tags:
---

　　有时候我们需要一个高度能随内容自动增加的输入框，`input` 显然不行，因为 `input` 里的文字是不换行的。文本域 `textarea` 里的文字倒是换行的，可一旦文字内容超过其高度，`textarea` 就会增加一个烦人的滚动条，这是很影响视觉的，就如同下面：
```html
<textarea cols="30" rows="3"></textarea>
```
<textarea cols="30" rows="3""></textarea>

　　那么有没有办法制作一个高度能随文字内容自动增加的输入框呢？答案是肯定的，下面介绍两种方式。

### 方式一

　　这种方式依然使用 `textarea`, 主要思想是我们将 `textarea` 放入一个容器中，同时在这个容器中放入一个隐藏的 div (visibility: hidden), 监听 `textarea` 的输入事件并将其中的文字动态的同步到隐藏的div中，这样div 就可以撑开容器，这时设置 `textarea` 的高度为 100% 并将其定位到容器的左上角，那么 `textarea` 的高度自然就是其中文字内容的高度了。

