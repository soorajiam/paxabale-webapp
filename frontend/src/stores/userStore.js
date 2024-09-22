import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const token = ref(localStorage.getItem('access_token') || '')
  const userId = ref(localStorage.getItem('user_id') || '')
  const name = ref(localStorage.getItem('user_name') || '')
  const username = ref(localStorage.getItem('username') || '')

  const isAuthenticated = computed(() => !!token.value)

  const setUser = (userData) => {
    token.value = userData.token
    userId.value = userData.userId
    name.value = userData.name
    username.value = userData.username

    localStorage.setItem('access_token', userData.token)
    localStorage.setItem('user_id', userData.userId)
    localStorage.setItem('user_name', userData.name)
    localStorage.setItem('username', userData.username)
  }

  const clearUser = () => {
    token.value = ''
    userId.value = ''
    name.value = ''
    username.value = ''

    localStorage.removeItem('access_token')
    localStorage.removeItem('user_id')
    localStorage.removeItem('user_name')
    localStorage.removeItem('username')
  }

  const register = async (userData) => {
    try {
      const response = await axios.post('/v1/auth/signup/', userData)
      if (response.status === 201) {
        setUser({
          token: response.data.token,
          userId: response.data.user.id,
          name: response.data.user.name,
          username: response.data.user.username
        })
        return true
      }
    } catch (error) {
      console.error('Registration error:', error)
      return false
    }
  }

  const login = async (credentials) => {
    try {
      const response = await axios.post('/v1/auth/login/', credentials)
      if (response.status === 200) {
        setUser({
          token: response.data.token,
          userId: response.data.user.id,
          name: response.data.user.name,
          username: response.data.user.username
        })
        return true
      }
    } catch (error) {
      console.error('Login error:', error)
      return false
    }
  }

  const loginWithOAuth = async (token, user) => {
    setUser({
      token: token,
      userId: user.id,
      name: user.name,
      username: user.username
    })
  }

  const logout = () => {
    clearUser()
  }

  const checkAuth = async () => {
    if (!token.value) return false
    try {
      const response = await axios.get('/v1/auth/user/', {
        headers: { Authorization: `Bearer ${token.value}` }
      })
      if (response.status === 200) {
        setUser({
          token: token.value,
          userId: response.data.id,
          name: response.data.name,
          username: response.data.username
        })
        return true
      }
    } catch (error) {
      console.error('Auth check error:', error)
      clearUser()
      return false
    }
  }

  return {
    token,
    userId,
    name,
    username,
    isAuthenticated,
    register,
    login,
    logout,
    checkAuth,
    loginWithOAuth,
    clearUser,
  }
})
