<template>
  <div id="app">
    <MyHeader></MyHeader>

    <ul>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>
</template>

<script>
import MyHeader from '@/components/MyHeader'

export default {
  name: 'app',
  components: {
    MyHeader
  }
};
</script>

<style>
/* 全局样式表 */

body{
  margin: 0px;
  font-size: 16px;
}

a {
  text-decoration: none;
  color: black;
}

button {
  cursor: pointer;
}

/* 测试 */

ul li:nth-child(1) {
  width: 200px;
  height: 30px;
  background-color: #A7C8F2;
}
ul li:nth-child(2) {
  width: 200px;
  height: 30px;
  background-color: #048ABF;
}
ul li:nth-child(3) {
  width: 200px;
  height: 30px;
  background-color: #027368;
}
ul li:nth-child(4) {
  width: 200px;
  height: 30px;
  background-color: #F25116;
}
ul li:nth-child(5) {
  width: 200px;
  height: 30px;
  background-color: #0D0D0D;
}

#app {
  width: 100%;

}
</style>

