<template>
  <div class="video-show">
    <header>
      <div>
        <h5>最新电影</h5>
        <a href>More</a>
      </div>
    </header>
    <div class="row">
      <VideoBox
        v-for="movieItem in movieItems"
        v-bind:key="movieItem.id"
        v-bind:href="movieItem.href"
        v-bind:imgSrc="movieItem.imgSrc"
        v-bind:name="movieItem.name"
        v-bind:actors="movieItem.actors"
      ></VideoBox>
    </div>
  </div>
</template>

<script>
import VideoBox from '@/components/VideoBox'

export default {
  props: ['movieItems'],
  components: {
    VideoBox
  }
};
</script>

<style>
.video-show .row {
  padding-left: 0.75rem;
  padding-bottom: 0.75rem;
  background-color: #fff;
  margin-bottom: 1.2rem;
}
@media (max-width: 767px) {
  .video-show .row {
    padding-left: 0.45rem;
  }
}

.video-show header {
  padding: 0rem 0.75rem;
  background-color: #fff;
}
@media (max-width: 767px) {
  .video-show header {
    padding: 0rem 0.45rem;
  }
}

.video-show header div {
  border-bottom: solid 1px #CDCDCD;
  padding: 0.4rem 0rem;
}

.video-show header div h5 {
  margin: 0px;
  font-size: 0.8rem;
  color: #414141;
  font-weight: 400;
  line-height: 0.8rem;
  display: inline-block;
  user-select: none;
}

.video-show header div a {
  font-size: 0.7rem;
  line-height: 1.2rem;
  float: right;
  margin-right: 0.5rem;
}

.video-show header div a:hover {
  color: #F50000;
}
</style>