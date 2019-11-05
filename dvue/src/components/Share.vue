<template>
  <ul class="share-box">
    <li v-on:click="shareToWeibo">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#weibo" />
      </svg>
      <span>微博</span>
    </li>
    <li v-on:click="shareToDouban">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#douban" />
      </svg>
      <span>豆瓣</span>
    </li>
    <li v-on:click="shareToTieba">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#tieba" />
      </svg>
      <span>贴吧</span>
    </li>
    <li v-on:mouseenter="shareToWeChat" v-on:mouseleave="shareToWeChat">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#wechat" />
      </svg>
      <span>微信</span>
      <div class="qrcode-box" v-bind:class="{show: showQRCode}">
        <p>微信扫一扫分享给好友</p>
        <div ref="qrcode"></div>
      </div>
    </li>
    <li v-on:click="shareToQQ">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#qq" />
      </svg>
      <span>QQ</span>
    </li>
    <li v-on:click="shareToQQZone">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#qqzone" />
      </svg>
      <span>空间</span>
    </li>
    <li v-on:click="shareToLink" title="复制链接地址">
      <svg width="40" height="40">
        <use xlink:href="../assets/icon/icon.svg#link" />
      </svg>
      <span>链接</span>
    </li>
    <input id="copy" ref="copy" >
  </ul>
</template>

<script>
import QRCode from "qrcodejs2";

export default {
  props: ["name", "href", "summary", "imgSrc"],

  data: function() {
    return {
      source: "https://zizaixian.top",
      desc: "我发现了一部超好看的影片，推荐给你吧！",
      showQRCode: false,
    };
  },

  mounted: function() {
    this.createQrcode(this.$refs.qrcode);
    this.$refs.copy.setAttribute('value',this.href);
  },

  methods: {
    shareToWeibo: function() {
      const link =
        `http://service.weibo.com/share/share.php?` +
        `url=${this.href}&title=${this.summary}` +
        `&pic=${this.imgSrc}&count=1`;
      window.open(link);
    },

    shareToDouban: function() {
      const link =
        `http://shuo.douban.com/!service/share?` +
        `href=${this.href}&name=${this.name}` +
        `&image=${this.imgSrc}&text=${this.summary}`;
      window.open(link);
    },

    shareToTieba: function() {
      const link =
        `http://tieba.baidu.com/f/commit/share/openShareApi?` +
        `url=${this.href}&title=${this.name}` +
        `&desc=${this.summary}&pic=${this.imgSrc}`;
      window.open(link);
    },

    shareToWeChat: function() {
      this.showQRCode = !this.showQRCode;
    },

    shareToQQ: function() {
      const link =
        `http://connect.qq.com/widget/shareqq/index.html?` +
        `url=${this.href}&title=${this.name}&source=${this.source}` +
        `&desc=${this.desc}&pics=${this.imgSrc}&summary=${this.summary}`;
      window.open(link);
    },

    shareToQQZone: function() {
      const link =
        `http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?` +
        `url=${this.href}&title=${this.name}&site=${this.source}` +
        `&desc=${this.desc}&pics=${this.imgSrc}&summary=${this.summary}`;
      window.open(link);
    },

    shareToLink: function() {
      this.$refs.copy.focus();
      this.$refs.copy.select();
      document.execCommand('copy');
    },

    createQrcode: function(dom) {
      new QRCode(dom, {
        text: this.href,
        width: 150,
        height: 150,
        colorDark: "#000000",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
      });
    }
  }
};
</script>

<style scoped>
.share-box {
  margin: 0px;
}
.share-box * {
  z-index: 1000;
}

.share-box li {
  display: inline-block;
  cursor: pointer;
  position: relative;
  padding: 6px;
}

.share-box li svg {
  vertical-align: middle;
}
.share-box li:hover svg{
  opacity: 0.8;
}

.share-box li span {
  display: block;
  color: #333;
  font-size: 12px;
  margin-top: 3px;
  text-align: center;
}

.qrcode-box {
  display: none;
  position: absolute;
  top: -225px;
  left: -75px;
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
}

.qrcode-box p {
  font-size: 14px;
  font-weight: 700;
  text-align: center;
  margin: 0px;
  padding: 10px 0px;
  border-bottom: 1px solid #e0e0e0;
}

.qrcode-box div {
  padding: 15px;
}

#copy {
  width: 1px;
  height: 1px;
  opacity: 0;
  z-index: -10;
}

.show {
  display: block;
}
</style>