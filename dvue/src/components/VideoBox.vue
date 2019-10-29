<template>
  <div class="videobox col-sm-4 col-md-3 col-lg-2">
    <div class="video-img">
      <a v-bind:href="href">
        <img v-bind:src="imgSrc" alt="loss">
        <span></span>
      </a>
    </div>
    <div class="video-info">
      <a v-bind:href="href">{{ name }}</a>
      <span>{{ actors }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ['href', 'imgSrc', 'name', 'actors']
}
</script>

<style>
.videobox {
  overflow: hidden;
  margin-top: 1rem;
  padding: 0rem 0.65rem;
  box-sizing: border-box;
}

@media (max-width: 767px) {
  .videobox {
    padding: 0rem 0.2rem;
  }
}


/* 视频图片  */
.video-img a {
  width: 100%;
  display: block;
  position: relative;
  height: 0px;
  padding-bottom: 138%;
}

.video-img a img {
  width: 100%;
}

.video-img span {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0px;
  top: 0px;
  display: none;
  background-image: url("../assets/icon/action.svg");
  background-repeat: no-repeat;
  background-size: 30% 30%;
  background-position: center;
  background-color: rgba(0,0,0,0.3);
}
.video-img a:hover span {
  display: block;
}

/* 视频名字、演员  */
.video-info {
  width: 100%;
}

.video-info a,
.video-info span {
  width: 100%;
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.video-info a {
  font-size: 0.8rem;
  padding: 0.3rem 0rem 0.2rem;
  color:#161616;
}
.video-info a:hover {
  color: #f50000;
  text-decoration: underline;
}

.video-info span {
  font-size: 0.6rem;
  color: #555555;
}
</style>