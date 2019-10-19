<template>
  <div id="app">
    <MyHeader></MyHeader>
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
:root {
  --main-color: #F50000;
  --header-height: 70px;
  --search-box-height: calc(var(--header-height) / 1.75);
  font-size: 10px;
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

#app {
  width: 100%;
}
</style>
