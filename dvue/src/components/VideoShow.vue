<template>
  <div class="video-show">
    <header>
      <div>
        <h5>{{ headerTip }}</h5>
        <a href>More ></a>
      </div>
    </header>
    <div class="row">
      <VideoBox
        v-for="videoItem in videoItems"
        v-bind:key="videoItem.id"
        v-bind:href="videoItem.href"
        v-bind:imgSrc="videoItem.imgSrc"
        v-bind:name="videoItem.name"
        v-bind:actors="videoItem.actors"
      ></VideoBox>
    </div>
  </div>
</template>

<script>
import VideoBox from '@/components/VideoBox'

export default {
  props: ['headerTip', 'videoItems'],
  components: {
    VideoBox
  }
};
</script>

<style>
.video-show .row {
  padding-bottom: 0.75rem;
  margin-bottom: 1.2rem;
}

.video-show header {
  padding: 0rem 0.375rem;
}

.video-show header div {
  border-bottom: solid 1px #CDCDCD;
  padding: 0.4rem 0rem;
}

.video-show header div h5 {
  margin: 0px;
  font-size: 1.2rem;
  color: #414141;
  font-weight: 400;
  line-height: 0.8rem;
  display: inline-block;
  user-select: none;
}

.video-show header div a {
  float: right;
  color:#555;
  font-size: 0.7rem;
  line-height: 1.2rem;
  margin-right: 0.5rem;
}
.video-show header div a:hover {
  color: var(--sub-color);
}
</style>