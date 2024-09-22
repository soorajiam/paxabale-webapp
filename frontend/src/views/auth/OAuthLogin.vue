<script setup>
// get token and user parameter from url and convert user to json
// use useerStore to login user
// redirect to home page
import { useUserStore } from '@/stores/userStore'
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const router = useRouter()
const userStore = useUserStore()

onMounted(() => {
  const token = new URLSearchParams(window.location.search).get('token')
  const user = JSON.parse(new URLSearchParams(window.location.search).get('user'))
  userStore.loginWithOAuth(token, user)
  router.push('/')
})
</script>
<template>
  <div>OAuth Login</div>

</template>