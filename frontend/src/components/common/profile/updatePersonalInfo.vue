<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';
import { useToast } from 'primevue/usetoast';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';

const userStore = useUserStore();
const toast = useToast();

const name = ref( '');
const username = ref('');
const email = ref('');
const bio = ref('');

onMounted(async () => {
  try {
    // await userStore.checkAuth();
    console.log('test', userStore.name);
    email.value = userStore.email || '';
    bio.value = userStore.bio || '';
    name.value = userStore.name || '';
    username.value = userStore.username || '';
  } catch (error) {
    console.error('Error fetching user data:', error);
    toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to fetch user data', life: 3000 });
  }
});

const updateProfile = async () => {
  try {
    await userStore.updateProfile({
      name: name.value,
      username: username.value,
      email: email.value,
      bio: bio.value
    });
    toast.add({ severity: 'success', summary: 'Success', detail: 'Profile updated successfully', life: 3000 });
  } catch (error) {
    console.error('Update profile error:', error);
    toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to update profile', life: 3000 });
  }
};
</script>

<template>
  <div class="p-fluid">
        <div class="p-field mb-4 w-96">
      <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Name</label>
      <InputText class="w-full" id="name" v-model="name" placeholder="Enter your name" />
    </div>
    <div class="p-field mb-4 w-96">
      <label for="username" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Username</label>
      <InputText class="w-full" id="username" v-model="username" placeholder="Enter your username" />
    </div>
    <div class="p-field mb-4 w-96">
      <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Email</label>
      <InputText class="w-full" id="email" v-model="email" placeholder="Enter your email" type="email" />
    </div>
    <div class="p-field mb-4 w-96">
      <label for="bio" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Bio</label>
      <Textarea class="w-full" id="bio" v-model="bio" rows="3" placeholder="Tell us about yourself" />
    </div>
    <Button label="Update Profile" @click="updateProfile" class="p-button-primary" />
  </div>
</template>
