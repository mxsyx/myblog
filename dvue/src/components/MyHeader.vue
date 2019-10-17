<!-- 页面头部 -->

<template>
  <div id="my-header">
    <div>
      <a href="/"><h1>白居易</h1></a>
      <small>浮云轻入鹤撩雾，青山深处自在仙</small>
    </div>
    <div id="search-box">
      <input type="text" placeholder="请输入您要搜索的内容..." name="search-content">
      <button type="submit">搜索</button>
    </div>

  </div>
</template>

<script>
export default {  
}
</script>

<style scoped>
#my-header {
  width: 100%;
  height: 70px;
  box-shadow: 0 0 6px rgba(0,0,0,0.25);
}

#my-header img {
  width: 40px;
  height: 40px;
}

#my-header h1 {
  display: inline-block;
  margin: 0px 15px;
  color: #048ABF;
  line-height: 70px;
}

#my-header small {
  color: #AAAAAA;
  user-select: none;
}

#search-box {
  width: 450px;
  height: 40px;
  position: absolute;
  display: inline-block;
  top: 15px;
  right: 75px;
}
@media screen and (max-width: 900px) {
  #search-box {
    display: none;
  }
}

#search-box input {
  width: 100%;
  height: 100%;
  padding-left: 10px;
  border: 2px solid #F25116;
  border-radius: 5px;
  box-sizing: border-box;
}

#search-box button {
  color: white;
  width: 70px;
  height: 40px;
  top: 0px;
  right: 0px;
  position: absolute;
  background: #F25116;
  border: none;
  border-radius: 0 5px 5px 0;
  box-sizing: border-box;
}

</style>