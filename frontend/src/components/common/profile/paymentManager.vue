<template>
    <div>
        <h1 class="text-2xl font-bold mb-4">Payment Manager</h1>
        <div class="subscription-toggle mb-4">
            <SelectButton v-model="subscriptionType" :options="subscriptionOptions" optionLabel="name" optionValue="value" />
        </div>
        <div class=" flex flex-col flex-wrap gap-4">
            <div v-for="plan in organizedPlans" :key="plan.name" class=" ml-12 w-96">
                <Card>
                    <template #title>
                        {{ plan.name }}
                    </template>
                    <template #content>
                        <p>{{ formatPrice(plan.price) }} / {{ subscriptionType }}</p>
                    </template>
                    <template #footer>
                        <Button label="Subscribe" @click="subscribe(plan)" />
                    </template>
                </Card>
            </div>
        </div>
  
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import SelectButton from 'primevue/selectbutton';
import Card from 'primevue/card';
import Button from 'primevue/button';
import { loadStripe } from '@stripe/stripe-js';

const payments = ref([]);
const subscriptionType = ref('monthly');
const subscriptionOptions = [
    { name: 'Monthly', value: 'monthly' },
    { name: 'Annual', value: 'annual' }
];

onMounted(async () => {
    await getPlans();
});

const getPlans = async () => {
    try {
        const response = await axios.get('payments/list-plans/');
        payments.value = response.data;
    } catch (error) {
        console.error('Error fetching plans:', error);
    }
};

const organizedPlans = computed(() => {
    const plans = {};
    payments.value.forEach(item => {
        const { name } = item;
        const { interval, amount } = item.plan_details;
        
        if (!plans[name]) {
            plans[name] = { name, monthly: null, annual: null };
        }
        
        if (interval === 'month') {
            plans[name].monthly = amount;
        } else if (interval === 'year') {
            plans[name].annual = amount;
        }
    });

    return Object.values(plans).map(plan => ({
        ...plan,
        price: subscriptionType.value === 'monthly' ? plan.monthly : plan.annual
    }));
});

const formatPrice = (amount) => {
    return `£${(amount / 100).toFixed(2)}`;
};

const subscribe = async (plan) => {
    try {
        const priceId = subscriptionType.value === 'monthly' ? 
            payments.value.find(p => p.name === plan.name && p.plan_details.interval === 'month').plan_details.id :
            payments.value.find(p => p.name === plan.name && p.plan_details.interval === 'year').plan_details.id;

        const response = await axios.post('payments/create-checkout-session/', {
            priceId: priceId
        });
        const { sessionId } = response.data;

        // Load Stripe.js
        const stripe = await loadStripe(import.meta.env.VITE_STRIPE_PUBLIC_KEY);

        if (stripe) {
            // Redirect to Stripe Checkout
            const { error } = await stripe.redirectToCheckout({ sessionId });
            if (error) {
                console.error('Error redirecting to Stripe:', error);
            }
        } else {
            console.error('Stripe.js failed to load');
        }
    } catch (error) {
        console.error('Error creating checkout session:', error);
    }
};
</script>

<style scoped>

</style>