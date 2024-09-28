import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../views/HomeView.vue')
  },
  {
    path: '/genomebrowser',
    name: 'genomebrowser',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/GenomeBrowser.vue')
  },
  {
    path: '/newproj',
    name: 'newproj',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/NewProjView.vue')
  },
  {
    path: '/newcall',
    name: 'newcall',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/NewCallView.vue')
  },
  {
    path: "/reads/:id",
    name: "variantreads",
    component: () => import('../views/ReadView.vue'),
    props: true
  },
  {
    path: "/calls/:id",
    name: "variantcalls",
    component: () => import('../views/CallView.vue'),
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   const cookieValue = document.cookie.split("; ")
//   .find(row => row.startsWith('authtoken='))
//   if (cookieValue) {
//   }
// })

export default router
