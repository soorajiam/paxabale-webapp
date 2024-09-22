<template>
  <div class="min-h-screen bg-gray-100 dark:bg-gray-800">
  
    <main>
      <div class=" ">
        
     
        <router-view></router-view>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">

import Toast from 'primevue/toast';

import axios from 'axios';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';

const API_ROOT_URL = import.meta.env.VITE_API_ROOT_URL || 'http://127.0.0.1:8000/api/';
const router = useRouter();
const userStore = useUserStore();


// Initialize Axios with base URL
axios.defaults.baseURL = API_ROOT_URL;

// Add request interceptor
axios.interceptors.request.use(
  (config) => {
    const token = userStore.token;
    const userId = userStore.userId;

    if (token && userId) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add response interceptor
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // Redirect to login page if unauthorized
      router.push('/login');
    }
    return Promise.reject(error);
  }
);

// Make axios instance available globally using Vue's provide/inject system
import { provide } from 'vue';

provide('api', axios);

onMounted(() => {
  useUserStore.api = axios;
});

// Components can now use the API by injecting it:
// import { inject } from 'vue';
// const api = inject('api');
</script>