<template>
  <div class="random">
    <header>
      <div class="row">
        <h5 class="col-lg-7 col-sm-8">
          {{ headerTip }}
        </h5>
        <div class="select visible-lg col-lg-1">
          <span>
            {{ typeActive }}
            <i class="fa fa-chevron-down" aria-hidden="true"></i>
          </span>
          <ul>
            <li v-for="type in types" 
                v-bind:key="type.key"
                v-on:click="changeActive('type', type)">
              {{ type }}
            </li>
          </ul>
        </div>
        <div class="select visible-lg col-lg-1">
          <span>
            {{ yearActive }}
            <i class="fa fa-chevron-down" aria-hidden="true"></i>
          </span>
          <ul>
            <li v-for="year in years"
                v-bind:key="year.key"
                v-on:click="changeActive('year', year)">
              {{ year }}
            </li>
          </ul>
        </div>
        <div class="select visible-lg col-lg-1">
          <span>
            {{ areaActive }}
            <i class="fa fa-chevron-down" aria-hidden="true"></i>
          </span>
          <ul>
            <li v-for="area in areas"
                v-bind:key="area.key"
                v-on:click="changeActive('area', area)">
              {{ area }}
            </li>
          </ul>
        </div>
        <button class="btn btn-random col-sm-3 col-lg-1">
          <i class="fa fa-random" aria-hidden="true"></i>
          换一部
        </button>
      </div>
    </header>
    <VideoInfo></VideoInfo>
  </div>
</template>

<script>
import VideoInfo from "@/components/VideoInfo";

export default {
  props: ['headerTip', 'types'],

  data: function() {
    return {
      years: ['2019','2018','2017','2016','2015','2014','2013','2012','2011','2010'],
      areas: ['大陆','香港','台湾','美国','法国','英国','日本','韩国','德国','泰国','印度',
              '意大利','西班牙','加拿大','其他'],
      typeActive: '类型',
      yearActive: '年代',
      areaActive: '地区',
    }
  },

  methods: {
    changeActive(which, active) {
      switch(which) {
        case 'type': this.typeActive = active; break;
        case 'year': this.yearActive = active; break;
        case 'area': this.areaActive = active; break;
      }
    }
  },

  components: {
    VideoInfo
  }
};
</script>

<style scoped>
.random {
  margin-bottom: 1.2rem;
}

.random header {
  padding: 0rem 0.375rem;
}

.random header > div {
  border-bottom: solid 1px #CDCDCD;
  padding: 0.4rem 0rem;
  margin-bottom: 0.5rem;
}

.random header > div h5 {
  margin: 0px;
  font-size: 1.2rem;
  color: #414141;
  font-weight: 400;
  line-height: 0.8rem;
  display: inline-block;
  user-select: none;
}

.select {
  position: relative;
  padding: 0rem 0.2rem;
  cursor: pointer;
}

.select span {
  display: block;
  color:#CCCCCC;
  padding: 0.3rem 0.4rem;
  font-size: 0.7rem;
  background-color: var(--main-color);
}

.select span i {
  float: right;
}

.select ul {
  width: 100%;
  margin: 0px; 
  max-height: 0px;
  overflow: hidden;
  position: absolute;
  vertical-align: middle;
  transition: all 0.4s ease-out;
}

.select ul li {
  color: #414141;
  padding: 0.3rem 0rem;
  text-align: center;
  font-size: 0.7rem;
  background-color: #fff;
}
.select ul li:hover {
  color: #ffffff;
  background-color: var(--third-color);
}

.select:hover ul {
  max-height: 200px;
}

.btn-random {
  font-size: 0.7rem;
  line-height: 0.7rem;
  font-weight: 700;
  background-color: var(--nav-color);
}
@media (max-width: 1119px) {
  .btn-random {
    line-height: 1.5rem;
  }
}
.btn-random:hover {
  box-shadow: 0 0 0.6rem var(--nav-color);
}
</style>