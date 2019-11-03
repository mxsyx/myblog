<template>
  <div id="app">
    <MyHeader></MyHeader>
    <Navigation></Navigation>
    <Lb></Lb>
    <Main></Main>
  </div>
</template>

<script>
import MyHeader from '@/components/MyHeader'
import Navigation from '@/components/Navigation'
import Lb from '@/components/Lb'
import Main from '@/components/Main'

export default {
  name: 'app',
  components: {
    MyHeader,
    Navigation,
    Lb,
    Main,
  }
};
</script>

<style>
/* 全局样式表 */
:root {
  font-size: 20px;
  --main-color: #34495E;
  --sub-color: #f50000;
  --third-color: #1B9AF7;
  --nav-color: #344950;
}

body{
  margin: 0px;
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