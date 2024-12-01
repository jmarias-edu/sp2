import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import VueCookies from "vue-cookies"
import api from "@/api/api.service";

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
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/workflow',
    name: 'workflow',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/WorkflowView.vue')
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
  },
  {
    path: "/admin",
    name: "adminview",
    component: () => import('../views/AdminView.vue'),
    beforeEnter: async (to, from, next) => {
      try {
        const response = await api.post('/google/check-admin/', {token: VueCookies.get('authtoken')});
        
        if (response.data.admin) {
          next();
        } else {
          alert('Access Denied');
          next('/');
        }
      } catch (error) {
        console.error('Error checking admin:', error);
        alert('Access Denied');
        next('/');
      }
    }
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
