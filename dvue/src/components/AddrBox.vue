<!-- 播放线路盒 -->

<template>
  <div class="addr-box">
    <header>
      <div>
        <h5>播放线路</h5>
        <div class="btn-box">
          <button
              class="btn btn-channel"
              v-for="channel in channels"
              v-bind:key="channel.key"
              v-on:click="changeChannel(channel.id)">
            线路 {{ channel.id + 1 }}
          </button>
        </div>
      </div>
    </header>
    <ul class="row channel-box"
        v-for="channel in channels"
        v-bind:key="channel.key"
        v-bind:class="{hidden: channel.hidden}">
      <li class="col-sm-3 col-md-2 col-lg-1"
          v-for="index in generateArray(channel.numEpisode)"
          v-bind:key="index.key">
        <a v-bind:href="`/play/${vid}/${channel.id}/${index}`">
          第 {{ index + 1 }} 集
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['vid'],
  
  data: function() {
    return {
      // 活动线路ID
      activeChannel: 0,
      channels: [
        {
          id: 0,
          hidden: true,
          numEpisode: 32
        },
        { 
          id: 1,
          hidden: true,
          numEpisode: 32
        },
        {
          id: 2,
          hidden: true,
          numEpisode: 32 
        },
        {
          id: 3,
          hidden: true,
          numEpisode: 32
        },
        {
          id: 4,
          hidden: true,
          numEpisode: 32
        },
        {
          id: 5,
          hidden: true,
          numEpisode: 32
        }
      ]
    }
  },

  mounted: function(){
    this.channels[this.activeChannel].hidden = false;
  },

  computers: {
    getPlayAddr(vid, channelId, index) {
      return `/play/${vid}/${channelId}/${index}`
    }
  },

  methods: {
    /**
     * 切换线路
     * @param {Number} channeId 线路ID
     */
    changeChannel: function(channelId) {
      this.channels[this.activeChannel].hidden = true;
      this.channels[channelId].hidden = false;
      this.activeChannel = channelId;
    },

    generateArray: function(n) {
      return Array.from(new Array(n).keys());
    }
  }
}
</script>

<style scoped>
.hidden {
  display: none !important;
}

.channel-box li {
  padding: 0.3rem;
  box-sizing: border-box;
}

.channel-box li a {
  display: block;
  color: #333333;
  text-align: center;
  font-size: 0.7rem;
  line-height: 1.7rem;
  border-radius: 0.25rem;
  background-color: #eee
}
.channel-box li a:hover {
  color: #fff;
  background-color: var(--third-color);
}

.addr-box {
  margin: 1rem 0rem;
}

.addr-box header {
  padding: 0rem 0.375rem;
}

.addr-box header > div {
  border-bottom: solid 1px #CDCDCD;
  padding: 0.4rem 0rem;
}

.addr-box header > div h5 {
  margin: 0px;
  font-size: 1.2rem;
  color: #414141;
  font-weight: 400;
  line-height: 0.8rem;
  display: inline-block;
  user-select: none;
}

.btn-box {
  float: right;
}
</style>