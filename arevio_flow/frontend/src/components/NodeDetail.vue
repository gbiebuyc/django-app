<template>
<div v-if="!node">Select a node.</div>
<div v-else>
    <h1>{{ node.name }}</h1>
    <p v-for="(paragraph, i) in node.content" :key='i'>
        {{ paragraph }}
    </p>
</div>
</template>

<script>
export default {
    props: {
        node: Object,
    }
}
</script>

<style>

</style>
