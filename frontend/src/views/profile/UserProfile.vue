<script setup>
import UserNavBar from '@/components/common/UserNavBar.vue'
import UpdatePersonalInfo from '@/components/common/profile/updatePersonalInfo.vue'
import PaymentManager from '@/components/common/profile/paymentManager.vue'
import { useUserStore } from '@/stores/userStore'
import { ref } from 'vue'
import { useToast } from 'primevue/usetoast'
import Toast from 'primevue/toast'

import Tabs from 'primevue/tabs';
import TabList from 'primevue/tablist';
import Tab from 'primevue/tab';
import TabPanels from 'primevue/tabpanels';
import TabPanel from 'primevue/tabpanel';

const toast = useToast()

const userStore = useUserStore()
const user = userStore.user

</script>

<template>
    <Toast />
    <UserNavBar />
  <div>
    <div class="container mx-auto dark:bg-gray-800">
      <div class="mt-10">

            <h1 class="text-3xl font-bold text-gray-800 dark:text-white">User Profile</h1>

            <Tabs class="mt-10" value="personal-info">
                <TabList>
                    <Tab value="personal-info">Personal Information</Tab>
                    <Tab value="change-password">Change Password</Tab>
                    <Tab value="delete-account">Payment and Subscription</Tab>
                </TabList>
                <TabPanels>
                    <TabPanel value="personal-info">
                        <div class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md">
                            <h1 class="text-xl mb-5 font-bold text-gray-800 dark:text-white">Personal Information</h1>
                            <UpdatePersonalInfo />
                        </div>
                    </TabPanel>
                    <TabPanel value="change-password">
                        <div class="bg-white p-8 rounded-lg shadow-md">
                            <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Change Password</h1>
                        </div>
                    </TabPanel>
                    <TabPanel value="delete-account">
                        <div class="bg-white p-8 rounded-lg shadow-md">
                            <h1 class="text-xl font-bold text-gray-800 dark:text-white">Payment and Subscription</h1>
                            <PaymentManager />
                        </div>
                    </TabPanel>
                </TabPanels>
            </Tabs>
      </div>
    </div>
  </div>
</template>