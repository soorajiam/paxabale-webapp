<script setup lang="ts">
import { ref } from 'vue'
import { useToast } from 'primevue/usetoast'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Divider from 'primevue/divider'
import Card from 'primevue/card'
import Password from 'primevue/password'
import { useDark } from '@vueuse/core'
import { useUserStore } from '@/stores/userStore'
import { useRouter } from 'vue-router'

import PublicNavBar from '@/components/common/PublicNavBar.vue'

const email = ref('')
const password = ref('')
const toast = useToast()
const userStore = useUserStore()
const router = useRouter()

const isDark = useDark()

const login = async () => {
  try {
    const success = await userStore.login({
      email: email.value,
      password: password.value
    })
    if (success) {
      toast.add({ severity: 'success', summary: 'Success', detail: 'Logged in successfully', life: 3000 })
      router.push('/') // Redirect to home page or dashboard
    } else {
      throw new Error('Login failed')
    }
  } catch (error) {
    console.error('Login error:', error)
    toast.add({ severity: 'error', summary: 'Error', detail: 'Login failed', life: 3000 })
  }
}

const loginWithGoogle = () => {
  // Implement Google login logic here
  const serverUrl = import.meta.env.VITE_API_ROOT_URL
  console.log('serverUrl: ', serverUrl)
  window.location.href = `${serverUrl}v1/auth/login/google/`
  console.log('Login with Google clicked')
  // You would typically redirect to your backend's Google OAuth endpoint
  // or use a library like vue3-google-login to handle the OAuth flow
}

</script>

<template>
  <PublicNavBar />
  <div class="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-500 to-purple-600">
    <Card class="w-full max-w-md shadow-2xl bg-white dark:bg-gray-800 rounded-lg overflow-hidden transform ">
      <template #title>
        <h2 class="text-3xl font-bold text-center mb-8 text-gray-800 dark:text-gray-200">Welcome Back</h2>
      </template>
      <template #content>
        <form @submit.prevent="login" class="space-y-6 px-6 py-4">
          <div>
            <label for="email" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Email</label>
            <InputText id="email" v-model="email" type="email" class="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <div>
            <label for="password" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Password</label>
            <Password id="password" v-model="password" toggleMask class="w-full p-password-input" inputClass="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <Button type="submit" label="Sign In" class="w-full p-3 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-md transition-colors duration-300" />
          <Divider align="center">
            <span class="text-gray-500 dark:text-gray-400">or</span>
          </Divider>
          <Button type="button" label="Sign in with Google" icon="pi pi-google" class="w-full p-3 bg-red-600 hover:bg-red-700 text-white font-bold rounded-md transition-colors duration-300" @click="loginWithGoogle" />
          <div class="text-center text-sm text-gray-600 dark:text-gray-400 mt-4">
            Don't have an account? 
            <router-link to="/register" class="text-blue-600 dark:text-blue-400 hover:underline font-medium">Create one now</router-link>
          </div>
        </form>
      </template>
    </Card>
  </div>
</template>