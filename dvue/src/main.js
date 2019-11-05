import Vue from 'vue';
import VueRouter from 'vue-router'
import routes from '@/router'
import App  from  '@/App.vue';

import '@/assets/saffron.css'
import '@/assets/font-awesome.min.css'


// 定义页面路由
Vue.use(VueRouter)
const router = new VueRouter({
  mode: 'history',
  routes: routes
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
