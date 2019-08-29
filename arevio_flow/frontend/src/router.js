import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import AnnualReport from './views/AnnualReport.vue'
import Profile from './views/Profile.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/annualreport',
      name: 'annualreport',
      component: AnnualReport
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
  ]
})
