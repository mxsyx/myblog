<template>
  <div id="app">
    <MyHeader></MyHeader>
    <Navigation></Navigation>
    <Lb></Lb>
  </div>
</template>

<script>
import MyHeader from '@/components/MyHeader'
import Navigation from '@/components/Navigation'
import Lb from '@/components/Lb'

export default {
  name: 'app',
  components: {
    MyHeader,
    Navigation,
    Lb,
  }
};
</script>

<style>
/* 全局样式表 */
:root {
  font-size: 20px;
  --main-color: #F50000;
  --nav-color: #344950
}

body{
  margin: 0px;
  background-color: rgb(240,240,240);
}

a {
  text-decoration: none;
  color: black;
}

button {
  cursor: pointer;
}

ul {
  list-style: none;
  padding-left: 0px;
}

#app {
  width: 100%;
}
</style>
