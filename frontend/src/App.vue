<template>
    <div
        id="app"
        class="h-full font-body"
    >
        <router-view />
    </div>
</template>

<script>
export default {
    name: "App",

    components: {},

    data() {
        return {};
    },

    mounted() {},
};
</script>

<style src="./assets/styles/tailwind.css">
body {
    font-family: "Heebo", "Helvetica", "Arial", "sans-serif";
    background-color: #f2f2f2;
}
</style>
