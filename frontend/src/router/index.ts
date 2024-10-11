import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/auth/LoginView.vue'
import RegisterView from '../views/auth/RegisterView.vue'
import OAuthLogin from '../views/auth/OAuthLogin.vue'
import UserDashboard from '../views/dashboard/UserDashboard.vue'
import UserProfile from '../views/profile/UserProfile.vue'
import FeaturesView from '../views/public/FeaturesView.vue'
import PricingView from '../views/public/PricingView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/features',
      name: 'features',
      component: FeaturesView
    },
    {
      path: '/pricing',
      name: 'pricing',
      component: PricingView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },

    {
      path: '/oauth/login',
      name: 'oauth-login',
      component: OAuthLogin
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: UserDashboard,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/dashboard/profile',
      name: 'profile',
      component: UserProfile,
      meta: {
        requiresAuth: true
      }
    },

  ]
})

export default router