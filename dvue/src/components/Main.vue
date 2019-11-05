<!-- Main Page -->

<template>
  <div class="page">
    <Carousel></Carousel>
    <VideoShow
      v-bind:headerTip="'最新电影'"
      v-bind:videoItems="movieItems"
    ></VideoShow>
    <Random 
      v-bind:headerTip="'随机看电影'"
      v-bind:types="movieTypes"
    ></Random>
    <VideoShow
      v-bind:headerTip="'最新电视剧'"
      v-bind:videoItems="tvItems"
    ></VideoShow>
    <Random
      v-bind:headerTip="'随机看电视剧'"
      v-bind:types="tvTypes"
    ></Random>
  </div>
</template>

<script>
import Carousel from '@/components/Carousel'
import VideoShow from '@/components/VideoShow'
import Random from '@/components/Random'

export default {
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
      tvItems: [
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H0c647ff943a24a54a4eb2fd1c26f9776J.jpg',
          name: '守望者 第一季',
          actors: '杰瑞米·艾恩斯 雷吉娜·金 叶海亚·阿卜杜勒-迈丁 周洪'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H1239deeef7044073a9101b8014b65608O.jpg',
          name: '请融化我',
          actors: '池昌旭 元真儿 尹世雅 林元熙'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H894e1cdebf38400baa7b31493e37e35b1.jpg',
          name: '我的事说来话长',
          actors: '生田斗真'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H6b860cc7439b4a638194d7319fa2030b7.jpg',
          name: '谍战深海之惊蛰',
          actors: '张若昀 王鸥 孙艺洲 阚清子'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H208fc9b5422444b784115123994c2a76m.jpg',
          name: '光荣时代',
          actors: '张译 黄志忠 潘之琳 薛佳凝'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/Hc2472615129a4b8d9830b5675efeeca9o.jpg',
          name: '还是不能结婚的男人',
          actors: '阿部宽 吉田羊 深川麻衣 塚本高史'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/HTB1kjuvTmzqK1RjSZFHq6z3CpXaY.jpg',
          name: '杰克·莱恩 第一季',
          actors: '约翰·卡拉辛斯基 梅纳·玛索德 戈兰·卡斯蒂克 玛丽-乔西·克罗兹'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/HTB1pE9BTjDpK1RjSZFrq6y78VXaW.jpg',
          name: '铁拳 第二季',
          actors: '菲恩·琼斯 杰西卡·斯特普 萨沙·达万 爱丽丝·伊芙'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H13d3e73f4afa4c97b0228b54386c4cdeP.jpg',
          name: '为全人类 第一季',
          actors: '乔尔·金纳曼 莎拉·琼斯 斯宾塞·加雷特 迈克尔·哈尔尼'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H27e9e3c484b24a80b52cf730f3d84fee5.jpg',
          name: '地狱之音',
          actors: 'Michael Wu 娜奥·提桑纳特 louis 麦琪·阿帕'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H453b67a0e2654770af7fdc9e5661fc23X.jpg',
          name: '诈骗操作团',
          actors: '李东健 全慧彬 金赛纶 金权'
        },
        {
          href: 'https://www.dandanzan.com/dianying/27795.html',
          imgSrc: 'https://ae01.alicdn.com/kf/H2660bbd74f5542cca123d68d236b12a9h.jpg',
          name: '哈林教父',
          actors: '福里斯特·惠特克 文森特·多诺费奥 伊芬什·哈德拉 Gregory Cioffi'
        },
      ],
      movieTypes: ['动作片','喜剧片','爱情片','科幻片','恐怖片','剧情片','战争片','动漫片','微电影'],
      tvTypes: ['国产剧','港台剧','日韩剧','欧美剧','动漫剧'],
    }
  },
  components: {
    Carousel,
    VideoShow,
    Random,
  }
}
</script>

<style>

</style>