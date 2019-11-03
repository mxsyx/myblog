<template>
  <div id="app">
    <MyHeader></MyHeader>
    <Navigation></Navigation>
    <Carousel></Carousel>
    <Main></Main>
  </div>
</template>

<script>
import MyHeader from '@/components/MyHeader'
import Navigation from '@/components/Navigation'
import Carousel from '@/components/Carousel'
import Main from '@/components/Main'

export default {
  name: 'app',
  components: {
    MyHeader,
    Navigation,
    Carousel,
    Main,
  },
  methods: {
    resize: function() {
	    const ua = navigator.userAgent;
      if(/Android|iPhone|iPod/i.test(ua))
        document.documentElement.style.fontSize = '16px'
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

/* 按钮样式 */
.btn {
  border: none;
  outline: none;
  color:#ffffff;
  cursor: pointer;
  border-radius: 5px;
  padding: 0rem 1rem;
  box-sizing: border-box;
  font-size: 0.7rem;
  line-height: 1.6rem;
  transition: all 0.1s linear;
  margin: 0px 8px;
}
@media (max-width: 1119px) {
  .btn {
    padding: 0rem 0.6rem;
  }
}
</style>