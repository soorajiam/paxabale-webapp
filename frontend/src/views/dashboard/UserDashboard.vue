<template>
    <UserNavBar />
  <div class="p-4">
    <h1 class="text-3xl font-bold mb-6">User Dashboard</h1>
    
    <div class="grid">
      <div class="col-12 md:col-6 lg:col-3 mb-4">
        <Card class="h-full">
          <template #title>Total Users</template>
          <template #content>
            <div class="text-4xl font-bold text-blue-600">1,234</div>
          </template>
        </Card>
      </div>
      
      <div class="col-12 md:col-6 lg:col-3 mb-4">
        <Card class="h-full">
          <template #title>Active Projects</template>
          <template #content>
            <div class="text-4xl font-bold text-green-600">42</div>
          </template>
        </Card>
      </div>
      
      <div class="col-12 md:col-6 lg:col-3 mb-4">
        <Card class="h-full">
          <template #title>Completed Tasks</template>
          <template #content>
            <div class="text-4xl font-bold text-orange-600">789</div>
          </template>
        </Card>
      </div>
      
      <div class="col-12 md:col-6 lg:col-3 mb-4">
        <Card class="h-full">
          <template #title>Revenue</template>
          <template #content>
            <div class="text-4xl font-bold text-purple-600">$52,890</div>
          </template>
        </Card>
      </div>
    </div>
    
    <div class="grid mt-6">
      <div class="col-12 lg:col-8 mb-4">
        <Card>
          <template #title>Monthly Activity</template>
          <template #content>
            <Chart type="line" :data="chartData" :options="chartOptions" class="h-30rem" />
          </template>
        </Card>
      </div>
      
      <div class="col-12 lg:col-4 mb-4">
        <Card>
          <template #title>Recent Activities</template>
          <template #content>
            <Timeline :value="timelineEvents" class="w-full md:w-20rem">
              <template #content="slotProps">
                <small class="text-color-secondary">{{ slotProps.item.date }}</small>
                <p class="mb-0">{{ slotProps.item.text }}</p>
              </template>
            </Timeline>
          </template>
        </Card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Card from 'primevue/card';
import Chart from 'primevue/chart';
import Timeline from 'primevue/timeline';

import UserNavBar from '@/components/common/userNavBar.vue';

const chartData = ref({
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'Users',
      data: [65, 59, 80, 81, 56, 55, 40],
      fill: false,
      borderColor: '#4bc0c0',
      tension: 0.4
    },
    {
      label: 'Projects',
      data: [28, 48, 40, 19, 86, 27, 90],
      fill: false,
      borderColor: '#565656',
      tension: 0.4
    }
  ]
});

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
});

const timelineEvents = ref([
  { date: '15 min ago', text: 'New project created' },
  { date: '2 days ago', text: 'Task completed' },
  { date: '5 days ago', text: 'New user registered' },
  { date: '1 week ago', text: 'Project milestone reached' },
]);
</script>
