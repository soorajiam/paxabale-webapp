import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './style.css';

//core CSS
import "primeicons/primeicons.css";

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import ToastService from 'primevue/toastservice';
import { createPinia } from 'pinia'



// This global declaration is not recommended for security reasons.
// It's better to use a more controlled approach like Vue's provide/inject system
// or a state management solution like Pinia or Vuex.
// If you need to use the API, consider injecting it in components where needed.

// Example of a safer approach:
// import { provide } from 'vue';
// import { createApi } from './api'; // Assume you have an api creation function
// const api = createApi();
// provide('api', api);

// Then in components where you need to use the API:
// import { inject } from 'vue';
// const api = inject('api');

const pinia = createPinia()

const app = createApp(App)
app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
})
app.use(ToastService)
app.use(pinia)
app.mount('#app');