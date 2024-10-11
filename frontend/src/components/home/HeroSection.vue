<template>

<section class="xl:bg-contain bg-top bg-no-repeat dark:bg-gray-900" style="background-image: url('');" x-data="{ mobileNavOpen: false }">
        <div class="container px-4 mx-auto">
          
          <div class="py-12 text-center">
            <div class="max-w-lg mx-auto mb-8">
              <h2 class="text-3xl md:text-4xl mb-4 font-bold font-heading dark:text-white">
                <span>The quick</span>
                <span class="text-blue-600 dark:text-blue-400">brown fox</span>
                <span>jumps over the lazy dog.</span>
              </h2>
              <p class="text-blueGray-400 dark:text-gray-300 leading-relaxed">The quick brown fox jumps over the lazy dog.</p>
            </div>
            <div><a class="block sm:inline-block py-4 px-8 mb-4 sm:mb-0 sm:mr-3 text-xs text-white text-center font-semibold leading-none bg-blue-600 hover:bg-blue-700 rounded" href="#">Check Now</a><a class="block sm:inline-block py-4 px-8 text-xs text-blueGray-500 dark:text-gray-300 hover:text-blueGray-600 dark:hover:text-gray-100 text-center font-semibold leading-none bg-white dark:bg-gray-800 rounded" href="#">Documentation</a></div>
          </div>
          <div class="relative max-w-3xl mt-6 mb-8 mx-auto">
            <img src="" alt="">
            <div class="absolute" style="top: 3%; left: 9%; width: 82%; height: 90%;">
              <img class="object-contain w-full h-full" src="" alt="">
            </div>
          </div>
          <div class="flex flex-wrap items-center justify-center max-w-4xl mx-auto pt-8 pb-12">
            <div class="w-1/2 md:w-1/3 lg:w-1/5 px-3 mb-8">
              <img class="mx-auto" src="" alt="">
            </div>
            <div class="w-1/2 md:w-1/3 lg:w-1/5 px-3 mb-8">
              <img class="mx-auto" src="" alt="">
            </div>
            <div class="w-1/2 md:w-1/3 lg:w-1/5 px-3 mb-8">
              <img class="mx-auto" src="" alt="">
            </div>
            <div class="w-1/2 md:w-1/3 lg:w-1/5 px-3 mb-8">
              <img class="mx-auto" src="" alt="">
            </div>
            <div class="hidden md:block w-1/2 md:w-1/3 lg:w-1/5 px-3 mb-8">
              <img class="mx-auto" src="" alt="">
            </div>
          </div>
        </div>
        <div :class="{'block': mobileNavOpen, 'hidden': !mobileNavOpen}" class="hidden fixed top-0 left-0 bottom-0 w-5/6 max-w-sm z-50">
          <div x-on:click="mobileNavOpen = !mobileNavOpen" class="fixed inset-0 bg-blueGray-800 opacity-25"></div>
          <nav class="relative flex flex-col py-6 px-6 w-full h-full bg-white dark:bg-gray-800 border-r dark:border-gray-700 overflow-y-auto">
            <div class="flex items-center mb-8">
              <a class="mr-auto text-3xl font-semibold leading-none dark:text-white" href="#">
                <img class="h-10" src="" alt="" width="auto">
              </a>
              <button x-on:click="mobileNavOpen = !mobileNavOpen">
                <svg class="h-6 w-6 text-blueGray-400 dark:text-gray-400 cursor-pointer hover:text-blueGray-500 dark:hover:text-gray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewbox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>
            <div>
              <ul>
                <li class="mb-1"><a class="block p-4 text-sm text-blueGray-500 dark:text-gray-400 hover:bg-blue-50 dark:hover:bg-gray-700 hover:text-blue-600 dark:hover:text-blue-300" href="#">Product</a></li>
                <li class="mb-1"><a class="block p-4 text-sm text-blueGray-500 dark:text-gray-400 hover:bg-blue-50 dark:hover:bg-gray-700 hover:text-blue-600 dark:hover:text-blue-300" href="#">Company</a></li>
                <li class="mb-1"><a class="block p-4 text-sm text-blueGray-500 dark:text-gray-400 hover:bg-blue-50 dark:hover:bg-gray-700 hover:text-blue-600 dark:hover:text-blue-300" href="#">About Us</a></li>
                <li class="mb-1"><a class="block p-4 text-sm text-blueGray-500 dark:text-gray-400 hover:bg-blue-50 dark:hover:bg-gray-700 hover:text-blue-600 dark:hover:text-blue-300" href="#">Features</a></li>
              </ul>
              <div class="mt-4 pt-6 border-t border-blueGray-100 dark:border-gray-700"><a class="block px-4 py-3 mb-3 text-xs text-center font-semibold leading-none bg-blue-600 hover:bg-blue-700 text-white rounded" href="#">Sign Up</a><a class="block px-4 py-3 mb-2 text-xs text-center text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-semibold leading-none border border-blue-200 dark:border-blue-700 hover:border-blue-300 dark:hover:border-blue-600 rounded" href="#">Log In</a></div>
            </div>
            <div class="mt-auto">
              <p class="my-4 text-xs text-blueGray-400 dark:text-gray-400">
                <span>Get in Touch</span>
                <a class="text-blue-600 dark:text-blue-400 hover:text-blue-600 dark:hover:text-blue-300 underline" href="#">info@example.com</a>
              </p>
              <a class="inline-block px-1" href="#">
                <img src="" alt="">
              </a>
              <a class="inline-block px-1" href="#">
                <img src="" alt="">
              </a>
              <a class="inline-block px-1" href="#">
                <img src="" alt="">
              </a>
            </div>
          </nav>
        </div>
      </section>

</template>

<script setup>
</script>