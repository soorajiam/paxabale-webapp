<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import Avatar from 'primevue/avatar';
import { useToast } from 'primevue/usetoast';
import Drawer from 'primevue/drawer';


const router = useRouter();
const userStore = useUserStore();
import { MagnifyingGlassIcon, HomeIcon, BriefcaseIcon, CheckCircleIcon, EnvelopeIcon, UserIcon, PowerIcon, Bars3Icon } from '@heroicons/vue/24/outline'

const username = computed(() => userStore.username);

const isDrawerOpen = ref(false);
const items = ref([
    {
        label: 'Dashboard',
        icon: 'heroicon',
        command: () => router.push('/dashboard')
    },
    {
        label: 'Projects',
        icon: 'heroicon',
        command: () => router.push('/projects')
    },
    {
        label: 'Tasks',
        icon: 'heroicon',
        command: () => router.push('/tasks')
    },
    {
        label: 'Messages',
        icon: 'heroicon',
        command: () => router.push('/messages')
    }
]);

const handleLogout = () => {
    console.log("Logging out")
    userStore.clearUser();
    router.push('/');
};

const handleProfile = () => {
    router.push('/dashboard/profile');
};

</script>

<template>

    <Drawer v-model:visible="isDrawerOpen" :show-close-icon="false" :close-icon="Bars3Icon">
        <template #default>
            <ul class="list-none p-0 m-0">
                <li v-for="item in items" :key="item.label" class="mb-2">
                    <a v-ripple @click="item.command" class="flex align-items-center p-3 cursor-pointer hover:bg-gray-100 rounded-md">
                        <component :is="item.icon === 'heroicon' ? 
                            (item.label === 'Dashboard' ? HomeIcon : 
                            item.label === 'Projects' ? BriefcaseIcon : 
                            item.label === 'Tasks' ? CheckCircleIcon : 
                            EnvelopeIcon) : 'span'" 
                            class="mr-2 w-5 h-5" 
                            aria-hidden="true" 
                        />
                        <span class="p-menuitem-text">{{item.label}}</span>
                    </a>
                </li>
            </ul>
        </template>
    </Drawer>
    <div class="card">
        <Menubar class="bg-primary">
            <template #start>
            <Button @click="isDrawerOpen = !isDrawerOpen" class="p-button-text">
                <Bars3Icon class="w-6 h-6 text-black dark:text-white" />
            </Button>
            </template>
            <template #end>
                <div class="flex items-center gap-2">
                    <Button @click="handleProfile" class="p-button-text flex items-center gap-2 cursor-pointer hover:bg-gray-200 p-2 rounded-md">
                        <UserIcon class="w-6 h-6 mr-2" style="color: #2a1261" />
                        <span class="font-bold">{{ username }}</span>
                    </Button>
                    
                    <Button @click="handleLogout" class="p-button-text flex items-center gap-2">
                        <PowerIcon class="w-5 h-5" />
                        <span>Logout</span>
                    </Button>
                    <MagnifyingGlassIcon class="w-6 h-6 text-white" />
                </div>
            </template>
        </Menubar>
    </div>

    
</template>

<style scoped>
.p-menubar {
    padding: 0.5rem 1rem;
    border-radius: 0;
}

.p-menubar .p-menuitem-link {
    padding: 0.75rem 1rem;
}

.p-menubar .p-menuitem-icon {
    color: var(--primary-color-text);
}

.p-menubar .p-menuitem-text {
    color: var(--primary-color-text);
}

.p-menubar .p-menuitem:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.p-button-text {
    color: var(--primary-color-text) !important;
}

.p-button-text:hover {
    background-color: rgba(255, 255, 255, 0.1) !important;
}
</style>
