<script setup lang="ts">

import axios from 'axios'
import { ref } from 'vue'
import { useToast } from 'primevue/usetoast'
import Toast from 'primevue/toast';
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Card from 'primevue/card'
import Divider from 'primevue/divider'
import Password from 'primevue/password'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'
import PublicNavBar from '@/components/common/PublicNavBar.vue'

const router = useRouter()
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const name = ref('')
const username = ref('')
// const bio = ref('')
const toast = useToast()

const userStore = useUserStore()

const register = async () => {
  console.log('register called')
  if (password.value !== confirmPassword.value) {
    console.log('passwords do not match')
    toast.add({ severity: 'error', summary: 'Error', detail: 'Passwords do not match', life: 3000 })
    return
  }
  try {
    const success = await userStore.register({
      email: email.value,
      password: password.value,
      name: name.value,
      username: username.value,
      // bio: bio.value
    })
    if (success) {
      toast.add({ severity: 'success', summary: 'Success', detail: 'Registration successful', life: 3000 })
      router.push('/login')
    } else {
      throw new Error('Registration failed')
      toast.add({ severity: 'error', summary: 'Error', detail: 'Registration failed', life: 3000 })
    }
  } catch (error) {
    console.error('Registration error:', error)
    toast.add({ severity: 'error', summary: 'Error', detail: 'Registration failed', life: 3000 })
  }
}

const signupWithGoogle = async () => {
  // access the .env file to get the server url
  const serverUrl = import.meta.env.VITE_API_ROOT_URL
  console.log('serverUrl: ', serverUrl)
  window.location.href = `${serverUrl}v1/auth/login/google/`
}

const navigateToLogin = () => {
  router.push('/login')
}
</script>

<template>
  <PublicNavBar />
  <Toast />
  <div class="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-500 to-purple-600">
    <Card class="w-full max-w-md shadow-2xl bg-white dark:bg-gray-800 rounded-lg overflow-hidden transform ">
      <template #title>
        <h2 class="text-3xl font-bold text-center mb-8 text-gray-800 dark:text-gray-200">Create an Account</h2>
      </template>
      <template #content>
        <form @submit.prevent="register" class="space-y-6 px-6 py-4">
          <div>
            <label for="name" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Name</label>
            <InputText id="name" v-model="name" class="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <div>
            <label for="username" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Username</label>
            <InputText id="username" v-model="username" class="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <!-- <div>
            <label for="bio" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Bio</label>
            <InputText id="bio" v-model="bio" class="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" />
          </div> -->
          <div>
            <label for="email" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Email</label>
            <InputText id="email" v-model="email" type="email" class="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <div>
            <label for="password" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Password</label>
            <Password id="password" v-model="password" toggleMask class="w-full p-password-input" inputClass="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <div>
            <label for="confirm-password" class="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Confirm Password</label>
            <Password id="confirm-password" v-model="confirmPassword" toggleMask class="w-full p-password-input" inputClass="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-500" required />
          </div>
          <Button type="submit" label="Sign Up" class="w-full p-3 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-md transition-colors duration-300" />
          <Divider align="center">
            <span class="text-gray-500 dark:text-gray-400">or</span>
          </Divider>
          <Button type="button" label="Sign up with Google" icon="pi pi-google" class="w-full p-3 bg-red-600 hover:bg-red-700 text-white font-bold rounded-md transition-colors duration-300" @click="signupWithGoogle" />
          <div class="text-center text-sm text-gray-600 dark:text-gray-400 mt-4">
            Already have an account? 
            <router-link to="/login" class="text-blue-600 dark:text-blue-400 hover:underline font-medium">Log in now</router-link>
          </div>
        </form>
      </template>
    </Card>
  </div>
</template>