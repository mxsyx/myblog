<template>
  <div class="share-box">
    <svg width="32" height="32">
      <use xlink:href="../assets/icon/icon.svg#weibo" />
    </svg>
    <svg width="32" height="32">
      <use xlink:href="../assets/icon/icon.svg#zhihu" />
    </svg>
    <svg width="32" height="32">
      <use xlink:href="../assets/icon/icon.svg#wechat" />
    </svg>
    <svg width="32" height="32">
      <use xlink:href="../assets/icon/icon.svg#qq" />
    </svg>
    <svg width="32" height="32">
      <use xlink:href="../assets/icon/icon.svg#wechat-friends" />
    </svg>
    <svg width="32" height="32">
      <use xlink:href="../assets/icon/icon.svg#qqzone" />
    </svg>
    <svg width="24" height="24">
      <use xlink:href="../assets/icon/icon.svg#phone" />
    </svg>
    <svg width="22" height="22">
      <use xlink:href="../assets/icon/icon.svg#link" />
    </svg>
  </div>
</template>

<script>
export default {
  methods: {
    shareToQQ: function() {

    }
  }
};
</script>

<style scoped>
.share-box svg{
  padding: 2px;
  cursor: pointer;
  vertical-align: middle;
}
</style>