import Home from '@/views/HomeView.vue'
import Page1 from '@/views/Page1View.vue'
import Page2 from '@/views/Page2View.vue'
import Login from '@/views/LoginView.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/page1',
    component: Page1,
    meta: { requiresAuth: true }
  },
  {
    path: '/page2',
    component: Page2,
    meta: { requiresAuth: true }
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

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.logado) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router
