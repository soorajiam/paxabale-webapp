<script setup lang="ts">
import publicNavBar from '@/components/common/publicNavBar.vue';
</script>

<template>
    <publicNavBar />

              
    <section class="py-20 xl:bg-contain bg-top bg-no-repeat" style="background-image: url('');" x-data="{ slideWidth: 0, activeSlide: 0, slideCount: 4 }">
        <div class="container px-4 mx-auto">
          <div class="text-center mb-8">
            <h2 class="max-w-lg mx-auto mb-4 text-4xl font-bold font-heading">
              <span>Start saving time today and</span>
              <span class="text-blue-600">choose</span>
              <span>your best plan</span>
            </h2>
            <p class="max-w-sm mx-auto text-lg text-blueGray-400">Best for freelance developers who need to save their time</p>
          </div>
          <div class="flex flex-wrap sm:justify-center mb-10">
            <label class="flex items-center mr-8 mb-2">
              <input type="radio" name="billing" value="1">
              <span class="mx-2 font-semibold">Monthly Billing</span>
              <span class="inline-flex items-center justify-center w-12 h-10 bg-blue-600 text-white font-semibold rounded">$59</span>
            </label>
            <label class="flex items-center mb-2">
              <input type="radio" name="billing" value="2">
              <span class="mx-2 font-semibold">Annual Billing</span>
              <span class="inline-flex items-center justify-center w-12 h-10 bg-blue-600 text-white font-semibold rounded">$99</span>
            </label>
          </div>
          <div class="flex flex-wrap bg-white rounded shadow">
            <div class="w-full md:w-1/2 lg:w-2/5 px-3">
              <div class="p-8 text-center">
                <span class="text-blueGray-400">Sign In</span>
                <h4 class="mb-6 text-2xl">Finish your payment</h4>
                <div class="flex mb-4 px-4 bg-blueGray-100 rounded">
                  <input class="w-full py-4 text-xs placeholder-blueGray-400 font-semibold leading-none bg-blueGray-100 outline-none" type="email" placeholder="name@email.com">
                  <svg class="h-6 w-6 ml-4 my-auto text-blueGray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewbox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"></path>
                  </svg>
                </div>
                <div class="flex mb-6 px-4 bg-blueGray-100 rounded">
                  <input class="w-full py-4 text-xs placeholder-blueGray-400 font-semibold leading-none bg-blueGray-100 outline-none" type="password" placeholder="Enter your password">
                  <button class="ml-4">
                    <svg class="h-6 w-6 my-auto text-blueGray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewbox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                    </svg>
                  </button>
                </div>
                <div class="text-left mb-5 text-sm text-blueGray-400">
                  <label>
                    <input type="checkbox" name="terms" value="1">
                    <span class="ml-1">I agree to terms and conditions.</span>
                  </label>
                </div>
                <button class="block w-full p-4 text-center text-xs text-white font-semibold leading-none bg-blue-600 hover:bg-blue-700 rounded">Purchase now</button>
              </div>
            </div>
            <div class="relative w-full md:w-1/2 lg:w-3/5 px-3 bg-blue-500 rounded-r overflow-hidden">
              <div class="max-w-sm px-12 pt-12">
                <span class="text-xs text-blue-200">Metis templates</span>
                <div class="overflow-hidden">
                  <div :style="'transform: translateX(-' + slideWidth + 'px)'" class="flex transition-transform duration-500 ease-in-out -m-10">
                      <div x-ref="slide1" class="flex-shrink-0 w-full p-10">
                          <h3 class="mb-4 text-4xl font-bold font-heading text-white">Best for freelance developers who need to save their time.</h3>
                      </div>
                      <div x-ref="slide2" class="flex-shrink-0 w-full p-10">
                          <h3 class="mb-4 text-4xl font-bold font-heading text-white">Efficiency Hacks: Tools for Freelance Developers</h3>
                      </div>
                      <div x-ref="slide3" class="flex-shrink-0 w-full p-10">
                          <h3 class="mb-4 text-4xl font-bold font-heading text-white">Streamlining Freelance Development</h3>
                      </div>
                      <div x-ref="slide4" class="flex-shrink-0 w-full p-10">
                          <h3 class="mb-4 text-4xl font-bold font-heading text-white">Productivity Boosters for Freelance Coders</h3>
                      </div>
                  </div>
                </div>
                <div class="space-x-2 mb-8">
                  <button class="inline-block h-2 w-2 bg-white rounded-full" :class="{ 'bg-blue-600': activeSlide!=0, 'bg-white': activeSlide==0 }" x-on:click="activeSlide = 0, slideWidth = $refs['slide1'].offsetWidth * 0"></button>
                  <button class="inline-block h-2 w-2 bg-blue-600 rounded-full" :class="{ 'bg-blue-600': activeSlide!=1, 'bg-white': activeSlide==1 }" x-on:click="activeSlide = 1, slideWidth = $refs['slide2'].offsetWidth * 1"></button>
                  <button class="inline-block h-2 w-2 bg-blue-600 rounded-full" :class="{ 'bg-blue-600': activeSlide!=2, 'bg-white': activeSlide==2 }" x-on:click="activeSlide = 2, slideWidth = $refs['slide3'].offsetWidth * 2"></button>
                  <button class="inline-block h-2 w-2 bg-blue-600 rounded-full" :class="{ 'bg-blue-600': activeSlide!=3, 'bg-white': activeSlide==3 }" x-on:click="activeSlide = 3, slideWidth = $refs['slide4'].offsetWidth * 3"></button>
                </div>
              </div>
              <div class="absolute right-0 bottom-0">
                <div class="flex items-center h-full">
                  <img class="h-80" src="" alt="">
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
</template>
