<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import { HomeIcon, InformationCircleIcon, CogIcon, EnvelopeIcon, LanguageIcon, GlobeAltIcon, ArrowRightOnRectangleIcon, UserPlusIcon, ArrowLeftOnRectangleIcon, ChartBarIcon } from '@heroicons/vue/24/outline';

const router = useRouter();
const userStore = useUserStore();

const isAuthenticated = computed(() => userStore.isAuthenticated);

const items = ref([
    {
        label: 'Home',
        icon: 'heroicon',
        command: () => router.push('/')
    },
    {
        label: 'About',
        icon: 'heroicon',
        command: () => router.push('/about')
    },
    {
        label: 'Services',
        icon: 'heroicon',
        items: [
            {
                label: 'Translation',
                icon: 'heroicon',
                command: () => router.push('/services/translation')
            },
            {
                label: 'Localization',
                icon: 'heroicon',
                command: () => router.push('/services/localization')
            }
        ]
    },
    {
        label: 'Contact',
        icon: 'heroicon',
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

</script>

<template>
    <div class="card">
        <Menubar :model="items" class="bg-primary">
            <template #start>
                <img alt="logo" src="" height="40" class="mr-2" />
            </template>
            <template #item="{ item }">
                <a v-ripple class="flex align-items-center p-menuitem-link">
                    <component :is="item.icon === 'heroicon' ? 
                        (item.label === 'Home' ? HomeIcon : 
                        item.label === 'About' ? InformationCircleIcon : 
                        item.label === 'Services' ? CogIcon : 
                        item.label === 'Contact' ? EnvelopeIcon :
                        item.label === 'Translation' ? LanguageIcon :
                        item.label === 'Localization' ? GlobeAltIcon : 'span') : 'span'" 
                        class="mr-2 w-5 h-5" 
                        aria-hidden="true" 
                    />
                    <span class="p-menuitem-text">{{item.label}}</span>
                </a>
            </template>
            <template #end>
                <div class="flex align-items-center gap-2">
                    <template v-if="!isAuthenticated">
                        <Button @click="handleLogin" class="p-button-text flex items-center gap-2">
                            <ArrowRightOnRectangleIcon class="w-5 h-5" />
                            <span>Login</span>
                        </Button>
                        <Button @click="handleRegister" class="p-button-text flex items-center gap-2">
                            <UserPlusIcon class="w-5 h-5" />
                            <span>Register</span>
                        </Button>
                    </template>
                    <template v-else>
                        <Button @click="handleLogout" class="p-button-text flex items-center gap-2">
                            <ArrowLeftOnRectangleIcon class="w-5 h-5" />
                            <span>Logout</span>
                        </Button>
                        <Button @click="handleDashboard" class="p-button-text flex items-center gap-2">
                            <ChartBarIcon class="w-5 h-5" />
                            <span>Dashboard</span>
                        </Button>
                    </template>
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

.p-menubar .p-submenu-list {
    background-color: var(--primary-color);
    border: none;
    box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12);
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
