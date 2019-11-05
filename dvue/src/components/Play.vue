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
        id: '9E2E3368B56CDBB4',
        api: 'https://api.prprpr.me/dplayer/',
        token: 'tokendemo',
        maximum: 1000,
        addition: ['https://api.bilibili.com/x/v1/dm/list.so?oid=125743280'],
        user: 'DIYgod',
        bottom: '15%',
        unlimited: true,
      },
      contextmenu: [
        {
            text: '内嵌视频地址',
            click: (player) => {
                console.log(player);
            },
        },
      ],
    };
    this.dp = new DPlayer(options);

  },

  components: {
    AddrBox,
  }
}
</script>

<style>

</style>