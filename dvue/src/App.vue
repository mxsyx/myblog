<template>
  <div id="app">
    <MyHeader></MyHeader>
    <Navigation></Navigation>
    <router-view></router-view>
    <MyBottom></MyBottom>
  </div>
</template>

<script>
import MyHeader from '@/components/MyHeader'
import Navigation from '@/components/Navigation'
import MyBottom from '@/components/MyBottom'

export default {
  name: 'app',
  components: {
    MyHeader,
    Navigation,
    MyBottom
  },
  methods: {
    resize: function() {
      const ua = navigator.userAgent;
      if(/Android|iPhone|iPod/i.test(ua)) {
        document.documentElement.style.fontSize = '16px'
      }
    }
  },
  mounted: function() {
    this.resize();
  },
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
  color: #000000;
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

.page {
  width: 90%;
  margin: auto;
  margin-top: 1.5rem;
}
</style>