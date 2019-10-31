<template>
  <div class="video-info row">
    <div class="video-info-l col-lg-2">
      <img alt="loss" src="https://ae01.alicdn.com/kf/H3025e6e7b68e4dfb8ad7af25c2220d42Z.jpg">
    </div>
    <div class="video-info-r col-lg-10">
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
          <span class="info-tip">年代：</span>
          <span class="info-content">
            <a href="">2019</a>
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
          <span class="info-tip">总播放量：</span>
          <span class="info-content">2020</span>
        </div>
      </div>
      <div class="row intro">
        <div class="col-lg-11">
          <span class="info-tip">简介：</span>
          <span class="info-content">警官德夫正在调查一宗双重谋杀案，只有两名证人，他们也是主要嫌疑人。嫌疑犯之一，著名的作家；另一个，是年轻的家庭主妇玛雅。不同的故事，却在同一个命运之夜联系到了一起，而背后的真相也远非表面这么简单。这是一部没有歌舞也没有外挂的印度电影，只有悬疑和逻辑推理。</span>
        </div>
        <i class="col-lg-1 fa fa-angle-down" title="详情"></i>
      </div>
      <div class="row">
        <div class="col-lg-3">
          <span class="info-tip">更新日期：</span>
          <span class="info-content">2019-10-30</span>
        </div>
      </div>

      <div>
        <button class="btn btn-play">
          <i class="fa fa-play"></i>
          <span> 立即播放</span>
        </button>
        <button class="btn btn-download">
          <i class="fa fa-download" aria-hidden="true"></i>
          <span> 下载</span>
        </button>
        <button class="btn btn-collection">
          <i class="fa fa-star"></i>
          <span> 收藏</span>
        </button>
        <button class="btn btn-score">
          <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
          <span> 顶 </span>
          <span>(0)</span>
        </button>
        <button class="btn btn-score">
          <i class="fa fa-thumbs-o-down" aria-hidden="true"></i>
          <span> 踩 </span>
          <span>(0)</span>
        </button>
        <button class="btn btn-share">
          <i class="fa fa-share-alt" aria-hidden="true"></i>
          <span> 分享</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.video-info {
  width: 100%;
  padding: 0.8rem;
  box-sizing: border-box;
  background: linear-gradient(to bottom, var(--main-color), var(--main-color), 20%,
                              var(--main-color), 20%,#ffffff);
  margin-bottom: 400px;
}

.video-info-l img {
  width: 100%;
  border-radius: 8px;
}

/* 右侧视频信息 */
.video-info-r {
  overflow: hidden;
  padding: 0rem 1rem;
  box-sizing: border-box;
}

.video-info-r h2 {
  color:#fff;
  font-size: 1.2rem;
  font-weight: 400;
  margin: 0.6rem 0rem;
}

.video-info-r > div {
  padding: 0.3rem 0rem;
}
.video-info-r > div:nth-child(2) {
  padding: 0.8rem 0rem 0.3rem;
}

.intro > div {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.intro > i {
  color: #444;
  font-size: 0.8rem;
  line-height: 1.2rem;
  cursor: pointer;
}
.intro > i:hover {
  color: var(--sub-color);
}

.info-tip {
  font-size: 0.8rem;
  color: #666;
}

.info-content,
.info-content a {
  font-size: 0.8rem;
  color: rgb(51,51,51);
}

.info-content a:hover {
  color: #F50000;
  text-decoration: underline;
}


/* 按钮组 */
.btn-play {
  background-color: var(--sub-color);
}
.btn-play:hover {
  box-shadow: 0 0 0.6rem var(--sub-color);
}

.btn-download {
  background-color: var(--main-color);
}
.btn-download:hover {
  box-shadow: 0 0 0.6rem var(--main-color);
}

.btn-collection {
  background-color: var(--third-color);
}
.btn-collection:hover {
  box-shadow: 0 0 0.6rem var(--third-color);
}

.btn-score {
  color: #333333;
  background-color: #EEEEEE;
  padding: 0rem 0.4rem;
}
.btn-score:hover {
  opacity: 0.8;
  box-shadow: 0 0 0.6rem var(--third-color);
}

.btn-share {
  color: #000;
  background-color: transparent;
}

</style>