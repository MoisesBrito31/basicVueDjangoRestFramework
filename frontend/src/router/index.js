import Home from '@/views/HomeView.vue'
import Page1 from '@/views/Page1View.vue'
import Page2 from '@/views/Page2View.vue'
import Login from '@/views/LoginView.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/page1',
    component: Page1
  },
  {
    path: '/page2',
    component: Page2
  },
  {
    path: '/login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
