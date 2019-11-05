// 页面路由配置

import Main from '@/components/Main'
import Info from '@/components/Info'
import Play from '@/components/Play'

const routes = [
  // 主页路由
  {
    path: '/', 
    component: Main 
  },
  // 信息页路由
  {
    path: '/info/:vid',
    component: Info,
    props: true
  },
  {
    path: '/play/:vid/:channel/:episode',
    component: Play,
    props: true
  },
]

export default routes;
