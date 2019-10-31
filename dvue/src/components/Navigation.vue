<template>
  <div id="nav">
    <div id="nav-header" class="visible-sm">
      <a href="">首页</a>
      <button id="nav-toggle" v-on:click="toggle">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
    </div>
    <ul id="nav-menu">
      <li>
        <a href="#" class="three-d active hidden-sm">
          <span class="three-d-box">
            <span class="front">首页</span>
            <span class="back">首页</span>
          </span>
        </a>
      </li>
      <li>
        <a href="#" class="three-d">
          <span class="three-d-box">
            <span class="front">分类</span>
            <span class="back">分类</span>
          </span>
        </a>
      </li>
      <li>
        <a href="#" class="three-d">
          <span class="three-d-box">
            <span class="front">电影▼</span>
            <span class="back">电影▼</span>
          </span>
        </a>
        <ul>
          <li v-for="movieItem in movieItems" v-bind:key="movieItem.id">
            <a href="#" class="three-d">
              <span class="three-d-box">
                <span class="front">{{ movieItem.name }}</span>
                <span class="back">{{ movieItem.name }}</span>
              </span>
            </a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#" class="three-d">
          <span class="three-d-box">
            <span class="front">电视剧▼</span>
            <span class="back">电视剧▼</span>
          </span>
        </a>
        <ul>
          <li v-for="tvItem in tvItems" v-bind:key="tvItem.id">
            <a href="#" class="three-d">
              <span class="three-d-box">
                <span class="front">{{ tvItem.name }}</span>
                <span class="back">{{ tvItem.name }}</span>
              </span>
            </a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#" class="three-d">
          <span class="three-d-box">
            <span class="front">留言</span>
            <span class="back">留言</span>
          </span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      navDisplay: true,
      movieItems: [
        { name: '动作片'},
        { name: '喜剧片'},
        { name: '爱情片'},
        { name: '科幻片'},
        { name: '恐怖片'},
        { name: '剧情片'},
        { name: '战争片'}
      ],
      tvItems: [
        { name: '国产剧'},
        { name: '港台剧'},
        { name: '日韩剧'},
        { name: '欧美剧'}
      ]
    }
  },
  methods: {
    toggle: function() {
      const display = this.navDisplay ? '30rem': '2rem';
      document.getElementById('nav').style.maxHeight = display;
      this.navDisplay = !this.navDisplay;
    }
  }
}
</script>

<style scoped>
#nav {
  max-height: 2rem;
  overflow: hidden; 
  background-color: var(--nav-color);
  transition: all 0.8s linear;
}

#nav-menu {
  margin: 0px auto;
}

@media (max-width: 767px) {
  #nav-header {
    height: 2rem;
  }

  #nav-header a {
    width: 5rem;
    height: 2rem;
    display: inline-block;
    color: white;
    line-height: 2rem;
    padding-left: 0.6rem;
  }

  #nav-toggle {
    height: 100%;
    padding: 0.45rem 0.5rem;
    background-color: transparent;
    float: right;
    border: none;
  }

  #nav-toggle:focus {
    outline: none;
  }

  #nav-toggle .icon-bar {
    width: 1rem;
    height: 0.1rem;
    display: block;
    border-radius: 1px;
    background-color: rgb(214,214,214);
  }

  #nav-toggle .icon-bar +.icon-bar {
    margin-top: 0.2rem;
  }
}

#nav-menu > li {
  float: left;
  box-sizing: border-box;
  background-color: var(--nav-color);
}
@media (max-width: 767px) {
  #nav-menu > li {
    float: none;
    padding-left: 1.2rem;
  }
}

.three-d {
  width: 5rem;
  height: 2rem;
  color: #fff;
  display: block;
  font-size: 0.9rem;
  line-height: 2rem;
  position: relative;
}
@media (max-width: 767px) {
  .three-d {
    width: 100%;
  }
}

.three-d:hover .three-d-box {
  transform: rotateX(90deg);
}

.three-d-box {
  width: 100%;
  height: 100%;
  display: block;
  transition: all 0.3s ease-out;
  transform-style: preserve-3d;
}

.front, .back {
  width: 100%;
  height: 100%;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  color: white;
  line-height: 2rem;
  text-align: center;
}
@media (max-width: 767px) {
  .front, .back {
    text-align: left;
  }
}

.front {
  background-color: var(--nav-color);
  transform: rotatex(0deg) translatez(1rem);
}

.back {
  background: var(--sub-color);
  transform: rotatex(-90deg) translatez(1rem);
}

#nav-menu ul {
  z-index: 15;
  position: absolute;
  line-height: 2rem;
  font-size: 0.9rem;
  transition: all 0.3s ease-in;
  transform-origin: 0px 0px;
  transform: rotateX(-90deg);
}
@media (max-width: 767px) {
  #nav-menu ul{
    display: none;
  }
  #nav-menu ul li {
    padding-left: 0.5rem;
  }
}

#nav-menu > li:hover ul {
  transform: rotateX(0deg);
}
@media (max-width: 767px) {
  #nav-menu > li:hover ul {
    display: block;
    position: static;
  }
}
</style>