<script setup lang="ts">

import Button from "primevue/button"
import { useUserStore } from "@/stores/userStore"
import PublicNavBar from "@/components/common/PublicNavBar.vue";

const userStore = useUserStore()


</script>

<template>
  <PublicNavBar />
  <div class="dark:bg-gray-900 dark:text-white">
    <Button label="Primary" class="dark:bg-blue-600 dark:hover:bg-blue-700"></Button>
    <Button severity="secondary" label="Secondary" class="dark:bg-gray-600 dark:hover:bg-gray-700"></Button>
    <Button severity="success" label="Success" class="dark:bg-green-600 dark:hover:bg-green-700"></Button>
    <Button severity="info" label="Info" class="dark:bg-cyan-600 dark:hover:bg-cyan-700"></Button>
    <Button severity="warn" label="Warn" class="dark:bg-yellow-600 dark:hover:bg-yellow-700"></Button>
    <Button severity="danger" label="Danger" class="dark:bg-red-600 dark:hover:bg-red-700"></Button>
    <Button severity="contrast" label="Contrast" class="dark:bg-gray-200 dark:text-gray-900 dark:hover:bg-gray-300"></Button>

    <h1 class="dark:text-white">Home</h1>
    <main class="container mx-auto p-4 dark:bg-gray-800">
      <h1 class="text-3xl font-bold mb-4 dark:text-white">Welcome to Open Translate</h1>
      <p class="mb-4 dark:text-gray-300">This is a simple Vue 3 app with Tailwind CSS.</p>
      <router-link to="/login" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2 dark:bg-blue-600 dark:hover:bg-blue-800">
        Login
      </router-link>
      <router-link to="/register" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded dark:bg-green-600 dark:hover:bg-green-800">
        Register
      </router-link>
      <p>User: {{ userStore.name }}</p>
      <p>Username: {{ userStore.username }}</p>
      <p>Token: {{ userStore.token }}</p>
      <p>User ID: {{ userStore.userId }}</p>
    </main>
  </div>
</template>