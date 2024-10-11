<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';
import { HomeIcon, InformationCircleIcon, CogIcon, EnvelopeIcon, LanguageIcon, GlobeAltIcon, ArrowRightOnRectangleIcon, UserPlusIcon, ArrowLeftOnRectangleIcon, ChartBarIcon } from '@heroicons/vue/24/outline';

const router = useRouter();
const userStore = useUserStore();

const isAuthenticated = computed(() => userStore.isAuthenticated);
const isMobileNavOpen = ref(false);
const isDarkMode = ref(false);

const items = ref([
    {
        label: 'Home',
        icon: HomeIcon,
        command: () => router.push('/')
    },
    {
        label: 'Features',
        icon: InformationCircleIcon,
        command: () => router.push('/features')
    },
    {
        label: 'Pricing',
        icon: InformationCircleIcon,
        command: () => router.push('/pricing')
    },
    {
        label: 'Contact',
        icon: EnvelopeIcon,
        command: () => router.push('/contact')
    }
]);

const handleLogin = () => {
    router.push('/login');
};

const handleRegister = () => {
    router.push('/register');
};

const handleLogout = () => {
    userStore.logout();
    router.push('/');
};

const handleDashboard = () => {
    router.push('/dashboard');
};

const toggleMobileNav = () => {
    isMobileNavOpen.value = !isMobileNavOpen.value;
};

const toggleDarkMode = () => {
    isDarkMode.value = !isDarkMode.value;
};

</script>

<template>
    <section :class="{ 'dark': isDarkMode }" class="bg-white dark:bg-gray-900">
        <div class="container px-4 mx-auto">
          <nav class="flex items-center py-6">
            <a class="text-3xl font-semibold leading-none text-gray-900 dark:text-white" href="#">
              <img class="h-10" src="" alt="" width="auto">
            </a>
            <div class="lg:hidden ml-auto">
              <button @click="toggleMobileNav" class="flex items-center py-2 px-3 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 rounded border border-blue-200 dark:border-blue-700 hover:border-blue-300 dark:hover:border-blue-600">
                <svg class="fill-current h-4 w-4" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <title>Mobile menu</title>
                  <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
                </svg>
              </button>
            </div>
            <ul class="hidden lg:flex items-center space-x-12 ml-auto mr-12">
              <li v-for="item in items" :key="item.label">
                <a class="text-sm text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white" href="#" @click="item.command">{{ item.label }}</a>
              </li>
            </ul>
            <div class="hidden lg:block">
              <button v-if="!isAuthenticated" @click="handleLogin" class="mr-2 inline-block px-4 py-3 text-xs text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-semibold leading-none border border-blue-200 dark:border-blue-700 hover:border-blue-300 dark:hover:border-blue-600 rounded">Log In</button>
              <button v-if="!isAuthenticated" @click="handleRegister" class="inline-block px-4 py-3 text-xs font-semibold leading-none bg-blue-600 hover:bg-blue-700 text-white rounded">Sign Up</button>
              <button v-if="isAuthenticated" @click="handleLogout" class="mr-2 inline-block px-4 py-3 text-xs text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-semibold leading-none border border-blue-200 dark:border-blue-700 hover:border-blue-300 dark:hover:border-blue-600 rounded">Log Out</button>
              <button v-if="isAuthenticated" @click="handleDashboard" class="inline-block px-4 py-3 text-xs font-semibold leading-none bg-blue-600 hover:bg-blue-700 text-white rounded">Dashboard</button>
            </div>
            <button @click="toggleDarkMode" class="ml-4 p-2 rounded-full bg-gray-200 dark:bg-gray-700">
              <svg v-if="isDarkMode" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-900" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
              </svg>
            </button>
          </nav>
        </div>
        <div :class="{'block': isMobileNavOpen, 'hidden': !isMobileNavOpen}" class="fixed top-0 left-0 bottom-0 w-5/6 max-w-sm z-50">
          <div @click="toggleMobileNav" class="fixed inset-0 bg-gray-800 opacity-25"></div>
          <nav class="relative flex flex-col py-6 px-6 w-full h-full bg-white dark:bg-gray-900 border-r dark:border-gray-700 overflow-y-auto">
            <div class="flex items-center mb-8">
              <a class="mr-auto text-3xl font-semibold leading-none text-gray-900 dark:text-white" href="#">
                <img class="h-10" src="" alt="" width="auto">
              </a>
              <button @click="toggleMobileNav">
                <svg class="h-6 w-6 text-gray-400 cursor-pointer hover:text-gray-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>
            <div>
              <ul>
                <li v-for="item in items" :key="item.label" class="mb-1">
                  <a @click="item.command" class="block p-4 text-sm text-gray-500 dark:text-gray-400 hover:bg-blue-50 dark:hover:bg-gray-800 hover:text-blue-600 dark:hover:text-blue-300" href="#">{{ item.label }}</a>
                </li>
              </ul>
              <div class="mt-4 pt-6 border-t border-gray-100 dark:border-gray-700">
                <button v-if="!isAuthenticated" @click="handleRegister" class="block w-full px-4 py-3 mb-3 text-xs text-center font-semibold leading-none bg-blue-600 hover:bg-blue-700 text-white rounded">Sign Up</button>
                <button v-if="!isAuthenticated" @click="handleLogin" class="block w-full px-4 py-3 mb-2 text-xs text-center text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-semibold leading-none border border-blue-200 dark:border-blue-700 hover:border-blue-300 dark:hover:border-blue-600 rounded">Log In</button>
                <button v-if="isAuthenticated" @click="handleLogout" class="block w-full px-4 py-3 mb-3 text-xs text-center font-semibold leading-none bg-blue-600 hover:bg-blue-700 text-white rounded">Log Out</button>
                <button v-if="isAuthenticated" @click="handleDashboard" class="block w-full px-4 py-3 mb-2 text-xs text-center text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-semibold leading-none border border-blue-200 dark:border-blue-700 hover:border-blue-300 dark:hover:border-blue-600 rounded">Dashboard</button>
              </div>
            </div>
          </nav>
        </div>
      </section>
</template>

<style scoped>
/* Removed unnecessary styles */
</style>
