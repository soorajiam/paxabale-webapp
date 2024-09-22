<template>
    <div class="container mx-auto p-4">
        <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
        <div class="bg-white shadow-md rounded-lg p-6">
            <h2 class="text-xl font-semibold mb-2">Daily Visitors</h2>
            <p class="text-4xl font-bold text-blue-600">{{ visitorCount }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const visitorCount = ref(0);

onMounted(() => {
    // Simulating API call to get visitor count
    // Replace this with actual API call in a real application
    setTimeout(() => {
        visitorCount.value = Math.floor(Math.random() * 1000) + 1;
    }, 1000);
});
</script>