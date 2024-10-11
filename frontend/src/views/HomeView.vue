<script setup lang="ts">

import Button from "primevue/button"
import { useUserStore } from "@/stores/userStore"
import PublicNavBar from "@/components/common/publicNavBar.vue";
import FeaturesSection from "@/components/home/FeaturesSection.vue";
import HeroSection from "@/components/home/HeroSection.vue";
import PaxStats from "@/components/home/PaxStats.vue";
import CTAhome from "@/components/home/CTAhome.vue";
import SubscribeToPax from "@/components/home/SubscribeToPax.vue";

const userStore = useUserStore()


</script>

<template>
  <PublicNavBar />
  <div class="dark:bg-gray-900 dark:text-white">
    <HeroSection />
    <FeaturesSection />
    <CTAhome />
    <PaxStats />
    <SubscribeToPax />
  </div>
</template>