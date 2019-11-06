<!-- Info Page -->

<template>
  <div class="page">
    <VideoInfo></VideoInfo>
    <AddrBox
      v-bind:vid="vid"
    ></AddrBox>
    <VideoShow
      v-bind:headerTip="'最新电影'"
      v-bind:videoItems="movieItems"
    ></VideoShow>
  </div>
</template>

<script>
import VideoInfo from "@/components/VideoInfo";
import AddrBox from '@/components/AddrBox';
import VideoShow from '@/components/VideoShow';


export default {
  props: ['vid'],

  data: function() {
    return {
      movieItems: [
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/HTB1gcadeliE3KVjSZFMq6zQhVXaf.jpg',
          name: '少年的你',
          actors: '周冬雨 易烊千玺 尹昉 黄觉'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H29ce761269bd4ce8ab0223ec94208afb2.jpg',
          name: '鲨海逃生',
          actors: '尼娅·朗 约翰·考伯特 苏菲·奈丽丝 科琳·福克斯'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H98633ba8726a421a8bcd163c0ee9b575w.jpg',
          name: '催眠·裁决',
          actors: '张家辉 张翰 秦沛 郑则仕'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H3025e6e7b68e4dfb8ad7af25c2220d42Z.jpg',
          name: '天作谜案',
          actors: '施坦·马洛萨 索娜什·辛哈 阿克夏耶·坎纳 曼迪拉·贝迪'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/Hb8c83887aa72450c8f4d9a17e27e65953.jpg',
          name: '小Q',
          actors: '任达华 梁咏琪 罗仲谦 杨采妮'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/Hbef00a55019f47798b0e50f3d0f9db30E.jpg',
          name: '犯罪现场',
          actors: '古天乐 宣萱 张继聪 谭耀文'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H302c9ed51b734840827e621ea0944b8b6.jpg',
          name: '帕瓦罗蒂',
          actors: '卢奇亚诺·帕瓦罗蒂 何塞·卡雷拉斯 普拉西多·多明戈 祖宾·梅塔'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H7695edf842af40868dcb9659a8f7b53aC.jpg',
          name: '爱情是什么',
          actors: '岸井雪乃 成田凌 深川麻衣 若叶龙也 保紫萌香 中島歩 片冈礼子 筒井真理子 江口德子'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H264a32837fc646648e8471dd64f98c0ci.jpg',
          name: '贞子',
          actors: '池田依来沙 塚本高史 清水寻也 姬岛妃花'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/HTB1j.SFThjaK1RjSZFAq6zdLFXaD.jpg',
          name: '末日',
          actors: '凯瑞·碧许 提奥·詹姆斯 福里斯特·惠特克 卡特琳娜·格兰厄姆'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/HTB1CPyoTgDqK1RjSZSyq6yxEVXax.jpg',
          name: '妖狐传',
          actors: '马倩倩 张竞达 王昭 朱利安'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/HTB1EQp5l_Zmx1VjSZFGq6yx2XXay.jpg',
          name: '陌生人2',
          actors: '克里斯蒂娜·亨德里克斯 拜莉·麦迪逊 马丁·亨德森 艾玛·贝洛米'
        },
      ],
      movieTypes: ['动作片','喜剧片','爱情片','科幻片','恐怖片','剧情片','战争片','动漫片','微电影'],
    }
  },

  components: {
    VideoInfo,
    AddrBox,
    VideoShow,
  }
}
</script>

<style>

</style>