<template>
  <ul class="share-box">
    <li v-on:click="shareToWeibo" title="分享到新浪微博">
      <svg width="32" height="32">
        <use xlink:href="../assets/icon/icon.svg#weibo" />
      </svg>
    </li>
    <li v-on:click="shareToDouban" title="分享到豆瓣">
      <svg width="34" height="34">
        <use xlink:href="../assets/icon/icon.svg#douban" />
      </svg>
    </li>
    <li v-on:mouseenter="shareToWeChat" v-on:mouseleave="shareToWeChat">
      <svg width="32" height="32">
        <use xlink:href="../assets/icon/icon.svg#wechat" />
      </svg>
      <div class="qrcode-box" v-bind:class="{show: showQRCode2}">
        <p>微信扫一扫分享给好友</p>
        <div ref="qrcode2"></div>
      </div>
    </li>
    <li v-on:click="shareToQQ" title="分享给QQ好友">
      <svg width="32" height="32">
        <use xlink:href="../assets/icon/icon.svg#qq" />
      </svg>
    </li>
    <li v-on:click="shareToQQZone" title="分享到QQ空间">
      <svg width="32" height="32">
        <use xlink:href="../assets/icon/icon.svg#qqzone" />
      </svg>
    </li>
    <li v-on:mouseenter="shareToPhone" v-on:mouseleave="shareToPhone">
      <svg width="24" height="24">
        <use xlink:href="../assets/icon/icon.svg#phone" />
      </svg>
      <div class="qrcode-box" v-bind:class="{show: showQRCode1}">
        <p>手机扫码观看</p>
        <div ref="qrcode1"></div>
      </div>
    </li>
    <li v-on:click="shareToLink" title="复制链接地址">
      <svg width="22" height="22">
        <use xlink:href="../assets/icon/icon.svg#link" />
      </svg>  
      <input id="copy" ref="copy" >
    </li>
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
      showQRCode1: false,
      showQRCode2: false,
    };
  },

  mounted: function() {
    this.createQrcode(this.$refs.qrcode1);
    this.createQrcode(this.$refs.qrcode2);
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

    shareToWeChat: function() {
      this.showQRCode2 = !this.showQRCode2;
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

    shareToPhone: function() {
      this.showQRCode1 = !this.showQRCode1;
    },

    shareToLink: function() {
      this.$refs.copy.focus();
      this.$refs.copy.select();
      document.execCommand('copy');
    },

    createQrcode: function(dom) {
      const qrcode = new QRCode(dom, {
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

.share-box li {
  display: inline-block;
  cursor: pointer;
  position: relative;
}
.share-box li:hover svg{
  opacity: 0.8;
}

.share-box li svg {
  vertical-align: middle;
  margin: 2px;
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

.show {
  display: block;
}

#copy {
  width: 1px;
  height: 1px;
  opacity: 0;
  z-index: -10;
}
</style>