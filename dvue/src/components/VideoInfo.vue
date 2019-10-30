<template>
  <div class="video-info row">
    <img class="col-lg-3" alt="loss"
         src="https://ae01.alicdn.com/kf/H3025e6e7b68e4dfb8ad7af25c2220d42Z.jpg">
    <div class="col-lg-9">
      <h2>天作谜案</h2>
      <div>
        <span class="info-tip">导演：</span>
        <span class="info-content">
          <a href="">阿沛·乔普拉</a>
        </span>
      </div>
      <div>
        <span class="info-tip">主演：</span>
        <span class="info-content">
          <a href="">施坦·马洛萨</a>、
          <a href="">索娜什·辛哈</a>、
          <a href="">阿克夏耶·坎纳</a>、
          <a href="">曼迪拉·贝迪</a>
        </span>
      </div>
      <div class="row">
        <div class="col-lg-2">
          <span class="info-tip">类型：</span>
          <span class="info-content">
            <a href="">悬疑</a>
          </span>
        </div>
        <div class="col-lg-2">
          <span class="info-tip">地区：</span>
          <span class="info-content">
            <a href="">美国</a>
          </span>
        </div>
        <div class="col-lg-2">
          <span class="info-tip">语言：</span>
          <span class="info-content">英语</span>
        </div>
        <div class="col-lg-2">
          <span class="info-tip">年代：</span>
          <span class="info-content">
            <a href="">2019</a>
          </span>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-3">
          <span class="info-tip">总播放量：</span>
          <span class="info-content">2020</span>
        </div>
        <div class="col-lg-3">
          <span class="info-tip">更新日期：</span>
          <span class="info-content">2019-10-30</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// 名字 导演 主演 类型 地区 语言 年代 更新 总播放量 点赞 吐槽
export default {

}
</script>

<style scoped>

.video-info {
  width: 100%;
  padding: 1rem;
  box-sizing: border-box;
  background-color: #fff;
}

.video-info img {
  height: 100%;
}

.video-info > div {
  padding: 0rem 0.8rem;
  box-sizing: border-box;
}

.video-info > div h2 {
  margin: 0.6rem 0rem;
  font-size: 1rem;
  font-weight: 400;
}

.video-info > div > div {
  padding: 0.2rem 0rem;
}

.info-tip {
  font-size: 0.8rem;
  color: #666;
}

.info-content,
.info-content a {
  font-size: 0.8rem;
  color: #252525;
}

.info-content a:hover {
  color: #F50000;
  text-decoration: underline;
}

</style>