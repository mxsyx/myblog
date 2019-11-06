<template>
  <div class="page">
    <div ref="player"></div>
    <AddrBox
      v-bind:vid="vid"
    ></AddrBox>
  </div>
</template>

<script>
import Hls from 'hls'
import DPlayer from 'dplayer';
import 'dplayer/dist/DPlayer.min.css';
import AddrBox from '@/components/AddrBox';

export default {
  props: ['vid'],

  mounted: function() {
    window.Hls = Hls;
    const options = {
      container: this.$refs.player,
      autoplay: false,
      screenshot: true,
      hotkey: true,
      volume: 0.7,
      video: {
        type: 'hls',
        url: 'https://vip.okokbo.com/20171214/EyioIJsB/index.m3u8',
      },
      danmaku: {
        id: '10101470022',
        api: 'https://dplayer.moerats.com/',
        token: 'tokendemo',
        maximum: 1000,
        user: 'DIYgod',
        bottom: '15%',
        unlimited: false,
      },
    };
    this.dp = new DPlayer(options);
    window.dp = this.dp;
  },

  components: {
    AddrBox,
  }
}
</script>

<style>

</style>